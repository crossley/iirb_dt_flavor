library('data.table')
library('ggplot2')
library('stringr')

rm( list = ls() )

fnames <- list.files(
  '../Data/EXP1_Data/',
  pattern='.csv',
  full.names=TRUE,
  recursive=TRUE)

ldf <- lapply(
  fnames,
  function(z) { z<-fread(z) })

ldf <- lapply(
  seq_along(ldf),
  function(z) {
    ldf[[z]][, sub := as.numeric(
                 unlist(str_extract_all(fnames[z], "[0-9]+")))[4]]
  })

d <- rbindlist(ldf, fill=TRUE)
setnames(d, "Correct?", "Correct")
setnames(d, "Block Number", "block")

## Participants 110-132 and 201-225 were run properly
good_subs <- c(seq(110, 132, 1), seq(201, 225, 1))

dd <- d[sub %in% good_subs]

ddd <- dd[, .(mean(Correct == "Y", na.rm = TRUE),
              sd(Correct == "Y", na.rm = TRUE)),
          .(block)]

ggplot(ddd, aes(x=block, y=V1)) +
  geom_line() +
  ylim(0.5,1.0)
