input <- jsonlite::fromJSON(file("stdin"))
if (!identical(input$version, 1L) ||
    !identical(input$method, "synthetic-mean-v1") ||
    !is.numeric(input$samples) || length(input$samples) != 3L ||
    any(!is.finite(input$samples))) {
  stop("Unsupported synthetic mean input")
}

cat(jsonlite::toJSON(
  list(version = 1L, method = "synthetic-mean-v1",
       count = length(input$samples), mean = mean(input$samples)),
  auto_unbox = TRUE, digits = NA
))
