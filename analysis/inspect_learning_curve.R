## NOTE: Learning curve figure
dd <- d[!(block %in% c(11,12)), mean(acc), .(rbii, condition, block, sub)]
ddd <- dd[, .(mean(V1), sd(V1)/sqrt(.N)), .(rbii, condition, block)]

ggplot(ddd, aes(x=block, y=V1, colour=condition)) +
  geom_line() +
  geom_errorbar(aes(ymin=V1-V2, ymax=V1+V2), width=0.2) +
  ylim(0.5,1.0) +
  scale_x_continuous(breaks = 1:12) +
  xlab('Block') +
  ylab('Accuracy') +
  facet_wrap(~rbii) +
  theme_classic() +
  theme(aspect.ratio = 1) +
  theme(strip.background = element_blank())
ggsave("../figs/learning_curves.pdf", width=8, height=4)

## NOTE: Begin Stats
## Within the II condition, is there a difference between dual tasks?
ddd <- dd[rbii=="II", mean(V1), .(rbii, condition, sub)]
fm <- lm(V1 ~ condition, data=ddd)
a <- anova(fm)
effect_size <- 1-var(residuals(fm))/var(model.response(model.frame(fm)))

paste(sep="", 'F(',
      round(a$Df[1]), ',',
      round(a$Df[2]), ') = ',
      format(round(a["F value"][1,1], 2), nsmall=2), ', p = ',
      format(round(a["Pr(>F)"][1,1], 2), nsmall=2), ', Omega = ',
      format(round(effect_size, 2), nsmall=2)
      )

t1 <- t.test(ddd[condition=="N", V1], ddd[condition=="S", V1])
t2 <- t.test(ddd[condition=="N", V1], ddd[condition=="V", V1])
t3 <- t.test(ddd[condition=="S", V1], ddd[condition=="V", V1])

paste(sep='', 't(',
      round(t1$parameter), ') = ',
      format(round(t1$statistic, 2), nsmall=2), ', p = ',
      format(round(t1$p.value, 2), nsmall=2), ', d = ',
      format(round(t1$statistic^2 / sqrt(t1$parameter), 2), nsmall=2)
      )

paste(sep='', 't(',
      round(t2$parameter), ') = ',
      format(round(t2$statistic, 2), nsmall=2), ', p = ',
      format(round(t2$p.value, 2), nsmall=2), ', d = ',
      format(round(t2$statistic^2 / sqrt(t2$parameter), 2), nsmall=2)
      )

paste(sep='', 't(',
      round(t3$parameter), ') = ',
      format(round(t3$statistic, 2), nsmall=2), ', p = ',
      format(round(t3$p.value, 2), nsmall=2), ', d = ',
      format(round(t3$statistic^2 / sqrt(t3$parameter), 2), nsmall=2)
      )


## Within the RB condition, is there a difference between dual tasks?
ddd <- dd[rbii=="RB", mean(V1), .(rbii, condition, sub)]
fm <- lm(V1 ~ condition, data=ddd)
a <- anova(fm)
effect_size <- 1-var(residuals(fm))/var(model.response(model.frame(fm)))

paste(sep="", 'F(',
      round(a$Df[1]), ',',
      round(a$Df[2]), ') = ',
      format(round(a["F value"][1,1], 2), nsmall=2), ', p = ',
      format(round(a["Pr(>F)"][1,1], 2), nsmall=2), ', Omega = ',
      format(round(effect_size, 2), nsmall=2)
      )

t1 <- t.test(ddd[condition=="N", V1], ddd[condition=="S", V1])
t2 <- t.test(ddd[condition=="N", V1], ddd[condition=="V", V1])
t3 <- t.test(ddd[condition=="S", V1], ddd[condition=="V", V1])

paste(sep='', 't(',
      round(t1$parameter), ') = ',
      format(round(t1$statistic, 2), nsmall=2), ', p = ',
      format(round(t1$p.value, 2), nsmall=2), ', d = ',
      format(round(t1$statistic^2 / sqrt(t1$parameter), 2), nsmall=2)
      )

paste(sep='', 't(',
      round(t2$parameter), ') = ',
      format(round(t2$statistic, 2), nsmall=2), ', p = ',
      format(round(t2$p.value, 2), nsmall=2), ', d = ',
      format(round(t2$statistic^2 / sqrt(t2$parameter), 2), nsmall=2)
      )

paste(sep='', 't(',
      round(t3$parameter), ') = ',
      format(round(t3$statistic, 2), nsmall=2), ', p = ',
      format(round(t3$p.value, 2), nsmall=2), ', d = ',
      format(round(t3$statistic^2 / sqrt(t3$parameter), 2), nsmall=2)
      )
