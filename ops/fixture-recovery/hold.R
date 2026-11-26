# Applied only by the recovery drill. Retain the real R calculation and deadline.
stopifnot(file.create("/tmp/rafiq-recovery-r-ready"))
while (!file.exists("/tmp/rafiq-recovery-r-release")) {
  Sys.sleep(0.05)
}
source("/fixture-recovery/synthetic_mean.R")
