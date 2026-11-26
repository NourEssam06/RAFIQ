import argparse
import sys
from dataclasses import dataclass
from html import escape
from io import BytesIO
from pathlib import Path
from typing import Literal, Self
from uuid import UUID

from pydantic import BaseModel, ConfigDict

from fixture.result import SYNTHETIC_SAMPLES, MeanResult

TITLE = "RAFIQ Synthetic Calculation"
DESCRIPTION = "This fixture compares PDF and Word output from one stored R result."
HEADERS = ("Measure", "Fixture result")
FONT = "DejaVu Sans"


class CompletedFixture(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)

    id: UUID
    status: Literal["completed"]
    result: MeanResult


@dataclass(frozen=True)
class RenderSnapshot:
    rows: tuple[tuple[str, str], ...]

    @classmethod
    def from_fixture(cls, payload: str | bytes) -> Self:
        result = CompletedFixture.model_validate_json(payload).result
        result.check_fixture_values()
        samples = ", ".join(str(sample) for sample in SYNTHETIC_SAMPLES)
        return cls((
            ("Samples", f"{samples} (unitless)"),
            ("Sample count", f"{result.count} samples"),
            ("Mean", f"{str(result.mean).removesuffix('.0')} (unitless)"),
            ("Method", result.method),
            ("Result version", str(result.version)),
        ))


def render_pdf(snapshot: RenderSnapshot) -> bytes:
    from weasyprint import HTML

    rows = "".join(
        f"<tr><td>{escape(label)}</td><td>{escape(value)}</td></tr>"
        for label, value in snapshot.rows
    )
    return HTML(string=f"""<!doctype html>
        <html lang="en">
        <head><meta charset="utf-8"><title>{TITLE}</title>
        <style>
          @page {{ size: A4; margin: 20mm; }}
          body {{ margin: 0; font: 11pt '{FONT}'; color: #222; }}
          h1 {{ margin: 0 0 8pt; font-size: 22pt; color: #000; }}
          p {{ margin: 0 0 14pt; }}
          table {{ width: 100%; border-collapse: collapse; }}
          th, td {{ border: 1px solid #d9d9d9; text-align: left; padding: 6pt; }}
          th {{ background: #eee; }}
          th:first-child {{ width: 34%; }}
        </style></head>
        <body>
          <h1>{TITLE}</h1>
          <p>{DESCRIPTION}</p>
          <table>
            <thead><tr><th scope="col">{HEADERS[0]}</th><th scope="col">{HEADERS[1]}</th></tr></thead>
            <tbody>{rows}</tbody>
          </table>
        </body></html>
    """).write_pdf()


def render_word(snapshot: RenderSnapshot) -> bytes:
    from docx import Document
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Mm, Pt, RGBColor

    document = Document()
    document.core_properties.title = TITLE
    document.core_properties.author = "RAFIQ"
    section = document.sections[0]
    section.page_width, section.page_height = Mm(210), Mm(297)
    section.top_margin = section.bottom_margin = section.left_margin = section.right_margin = Mm(20)

    normal = document.styles["Normal"]
    normal.font.name, normal.font.size = FONT, Pt(11)
    title = document.styles["Title"]
    title.font.name = FONT
    fonts = title.element.xpath("./w:rPr/w:rFonts")[0]
    for theme_font in ("asciiTheme", "hAnsiTheme", "eastAsiaTheme", "cstheme"):
        fonts.attrib.pop(qn(f"w:{theme_font}"), None)
    for element in title.element.xpath("./w:pPr/w:pBdr"):
        element.getparent().remove(element)
    heading = document.add_paragraph(TITLE, style=title).runs[0]
    heading.font.name, heading.font.size, heading.bold = FONT, Pt(22), True
    heading.font.color.rgb = RGBColor(0, 0, 0)
    document.add_paragraph(DESCRIPTION)

    table = document.add_table(rows=1, cols=2)
    table.autofit = False
    widths = (Mm(58), Mm(112))
    for column, width in zip(table.columns, widths, strict=True):
        column.width = width
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "bottom", "left", "right", "insideH", "insideV"):
        border = OxmlElement(f"w:{edge}")
        border.set(qn("w:val"), "single")
        border.set(qn("w:sz"), "4")
        border.set(qn("w:color"), "D9D9D9")
        borders.append(border)
    table._tbl.tblPr.insert_element_before(borders, "w:tblLook")

    header = table.rows[0]
    header._tr.get_or_add_trPr().append(OxmlElement("w:tblHeader"))
    for index, values in enumerate((HEADERS, *snapshot.rows)):
        row = header if index == 0 else table.add_row()
        for cell, width, value in zip(row.cells, widths, values, strict=True):
            cell.width = width
            paragraph = cell.paragraphs[0]
            paragraph.paragraph_format.space_before = Pt(5)
            paragraph.paragraph_format.space_after = Pt(5)
            paragraph.add_run(value).bold = index == 0

    output = BytesIO()
    document.save(output)
    return output.getvalue()


def main() -> None:
    parser = argparse.ArgumentParser(description="Render the completed local fixture from stdin")
    parser.add_argument("output", type=Path, help="existing output directory")
    args = parser.parse_args()
    try:
        snapshot = RenderSnapshot.from_fixture(sys.stdin.buffer.read())
    except ValueError:
        parser.error("expected a completed synthetic fixture with a compatible R result")

    pdf, word = render_pdf(snapshot), render_word(snapshot)
    (args.output / "synthetic-mean.pdf").write_bytes(pdf)
    (args.output / "synthetic-mean.docx").write_bytes(word)


if __name__ == "__main__":
    main()
