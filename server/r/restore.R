cellar <- tempfile("rafiq-r-sources-")
dir.create(cellar)

download_source <- function(package, version, sha256) {
  archive <- paste0(package, "_", version, ".tar.gz")
  target <- file.path(cellar, archive)
  base <- "https://cran.r-project.org/src/contrib"
  tryCatch(
    download.file(paste(base, archive, sep = "/"), target, mode = "wb", quiet = TRUE),
    error = function(error) {
      download.file(paste(base, "Archive", package, archive, sep = "/"), target,
                    mode = "wb", quiet = TRUE)
    }
  )
  digest <- system2("sha256sum", shQuote(target), stdout = TRUE)
  if (!startsWith(digest, paste0(sha256, " "))) {
    stop("Unexpected source archive for ", package)
  }
  target
}

renv_source <- download_source(
  "renv", "1.3.1", "e16281908ddf0ed6f8f6f8ad3f2cc4788af6de04c1ab223517aa1cc9acb30731"
)
invisible(download_source(
  "jsonlite", "2.0.0", "75eb910c82b350ec33f094779da0f87bff154c232e4ae39c9896a9b89f3ac82d"
))

library_path <- "/opt/rafiq-r"
install.packages(renv_source, lib = library_path, repos = NULL, type = "source")
Sys.setenv(RENV_PATHS_CELLAR = cellar)
renv::restore(project = "/app", library = library_path, prompt = FALSE)
stopifnot(packageVersion("renv") == "1.3.1", packageVersion("jsonlite") == "2.0.0")
