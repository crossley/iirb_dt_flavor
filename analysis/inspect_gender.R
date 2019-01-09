d[, gender := ifelse(gender=="Female", "f", gender)]
d[, gender := ifelse(gender=="female", "f", gender)]
d[, gender := ifelse(gender=="m", "m", gender)]
d[, gender := ifelse(gender=="M", "m", gender)]
d[, gender := ifelse(gender=="Male", "m", gender)]
d[, gender := ifelse(gender=="f", "f", gender)]
d[, gender := ifelse(gender=="male", "m", gender)]

dd <- d[gender=="f" | gender=="m"]

ddd <- dd[, gender[1], .(sub, cndname)][, .N, .(V1, cndname)]
setnames(ddd, 'V1', 'gender')
ggplot(ddd, aes(cndname, N)) +
  geom_bar(stat="identity",
           colour="black",
           position='dodge',
           width=0.8,
           aes(fill=gender)) +
  ylab('Number of Participants') +
  xlab('Condition') +
  theme_classic() +
  theme(aspect.ratio = 1) +
  theme(strip.background = element_blank())
ggsave("../figs/gender.pdf", width=8, height=4)

