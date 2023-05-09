parity <- function(number) {
    return (if (as.integer(number) %% 2 == 0) "even" else "odd")
}

lambdr::start_lambda()
