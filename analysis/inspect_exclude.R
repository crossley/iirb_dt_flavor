dtaccthresh <- seq(0.0, 0.8, 0.1)
record = list()
i <- 1
for(thresh in dtaccthresh) {
  dd <- d[dtacc >= thresh | cndname %in% c("N-RB", "N-II")]

  ddd <- dd[, mean(acc), .(rbii, condition, block, sub)]
  dddd <- ddd[, .(mean(V1), sd(V1)/sqrt(.N)), .(rbii, condition, block)]

  dddd[, exclusion_thresh := thresh]
  record[[i]] <- dddd
  i <- i + 1
}

d_exc <- rbindlist(record)

ggplot(d_exc, aes(x=block, y=V1, colour=condition)) +
  geom_line() +
  geom_errorbar(aes(ymin=V1-V2, ymax=V1+V2), width=0.2) +
  ylim(0.5,1.0) +
  scale_x_continuous(breaks = 1:12) +
  xlab('Block') +
  ylab('Accuracy') +
  facet_wrap(~exclusion_thresh*rbii, ncol=6) +
  theme_classic() +
  theme(aspect.ratio = 1) +
  theme(strip.background = element_blank())
ggsave("../figs/learning_curves_exc.pdf", width=12, height=8)
