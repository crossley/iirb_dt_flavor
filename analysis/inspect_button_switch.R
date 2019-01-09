## NOTE: cost as difference score
dd <- d[block %in% c(10,11), mean(acc), .(rbii, condition, cndname, block, sub)]

bs <- dd[, mean(V1[block==10] - V1[block==11], na.rm=TRUE),
         .(rbii, condition, cndname, sub)]

bss <- bs[, .(mean(V1, na.rm=TRUE),
                sd(V1, na.rm=TRUE)/sqrt(.N)), .(rbii, condition, cndname)]

ggplot(bss, aes(x=condition, y=V1, fill=condition)) +
  geom_bar(stat="identity", colour='Black', width=0.8) +
  geom_errorbar(aes(ymin=V1-V2, ymax=V1+V2), width=0.05) +
  geom_hline(yintercept=0.0) +
  xlab('Block') +
  ylab('Button-Switch Cost: Pre - Post') +
  facet_wrap(~rbii) +
  theme_classic() +
  theme(aspect.ratio = 1) +
  theme(strip.background = element_blank())
ggsave("../figs/bs_cost.pdf", width=8, height=4)

## NOTE: Are any bs-cost significantly different from zero?
bs[, paste(sep='', 't(',
           round(t.test(V1)$parameter), ') = ',
           format(round(t.test(V1)$statistic, 2), nsmall=2), ', p = ',
           format(round(t.test(V1)$p.value, 2), nsmall=2), ', d = ',
           format(round(t.test(V1)$statistic^2 / sqrt(t.test(V1)$parameter), 2), nsmall=2)
           ),
   .(cndname)]

## NOTE: Is the bs-cost different in the RB-V vs RB-S condition?
x <- bs[cndname == "V-RB", V1]
y <- bs[cndname == "S-RB", V1]
paste(sep='', 't(',
      round(t.test(x, y)$parameter), ') = ',
      format(round(t.test(x, y)$statistic, 2), nsmall=2), ', p = ',
      format(round(t.test(x, y)$p.value, 2), nsmall=2), ', d = ',
      format(round(
        t.test(x, y)$statistic^2 /
                            sqrt(t.test(x, y)$parameter), 2), nsmall=2))

x <- bs[cndname == "N-RB", V1]
y <- bs[cndname == "S-RB", V1]
paste(sep='', 't(',
      round(t.test(x, y)$parameter), ') = ',
      format(round(t.test(x, y)$statistic, 2), nsmall=2), ', p = ',
      format(round(t.test(x, y)$p.value, 2), nsmall=2), ', d = ',
      format(round(
        t.test(x, y)$statistic^2 /
                    sqrt(t.test(x, y)$parameter), 2), nsmall=2))

x <- bs[cndname == "V-RB", V1]
y <- bs[cndname == "N-RB", V1]
paste(sep='', 't(',
      round(t.test(x, y)$parameter), ') = ',
      format(round(t.test(x, y)$statistic, 2), nsmall=2), ', p = ',
      format(round(t.test(x, y)$p.value, 2), nsmall=2), ', d = ',
      format(round(
        t.test(x, y)$statistic^2 /
                    sqrt(t.test(x, y)$parameter), 2), nsmall=2))

## NOTE: Is the bs-cost different in the II-V vs II-S condition?
x <- bs[cndname == "V-II", V1]
y <- bs[cndname == "S-II", V1]
paste(sep='', 't(',
      round(t.test(x, y)$parameter), ') = ',
      format(round(t.test(x, y)$statistic, 2), nsmall=2), ', p = ',
      format(round(t.test(x, y)$p.value, 2), nsmall=2), ', d = ',
      format(round(
        t.test(x, y)$statistic^2 /
                            sqrt(t.test(x, y)$parameter), 2), nsmall=2))

x <- bs[cndname == "N-II", V1]
y <- bs[cndname == "S-II", V1]
paste(sep='', 't(',
      round(t.test(x, y)$parameter), ') = ',
      format(round(t.test(x, y)$statistic, 2), nsmall=2), ', p = ',
      format(round(t.test(x, y)$p.value, 2), nsmall=2), ', d = ',
      format(round(
        t.test(x, y)$statistic^2 /
                    sqrt(t.test(x, y)$parameter), 2), nsmall=2))

x <- bs[cndname == "V-II", V1]
y <- bs[cndname == "N-II", V1]
paste(sep='', 't(',
      round(t.test(x, y)$parameter), ') = ',
      format(round(t.test(x, y)$statistic, 2), nsmall=2), ', p = ',
      format(round(t.test(x, y)$p.value, 2), nsmall=2), ', d = ',
      format(round(
        t.test(x, y)$statistic^2 /
                    sqrt(t.test(x, y)$parameter), 2), nsmall=2))


## ## Within the RB condition, is there a difference between dual tasks?
## ddd <- dd[rbii=="RB", mean(V1), .(rbii, condition, sub)]
## fm <- lm(V1 ~ condition, data=ddd)
## a <- anova(fm)
## effect_size <- 1-var(residuals(fm))/var(model.response(model.frame(fm)))

## paste(sep="", 'F(',
##       round(a$Df[1]), ',',
##       round(a$Df[2]), ') = ',
##       format(round(a["F value"][1,1], 2), nsmall=2), ', p = ',
##       format(round(a["Pr(>F)"][1,1], 2), nsmall=2), ', Omega = ',
##       format(round(effect_size, 2), nsmall=2)
##       )

## t1 <- t.test(ddd[condition=="N", V1], ddd[condition=="S", V1])
## t2 <- t.test(ddd[condition=="N", V1], ddd[condition=="V", V1])
## t3 <- t.test(ddd[condition=="S", V1], ddd[condition=="V", V1])

## paste(sep='', 't(',
##       round(t1$parameter), ') = ',
##       format(round(t1$statistic, 2), nsmall=2), ', p = ',
##       format(round(t1$p.value, 2), nsmall=2), ', d = ',
##       format(round(t1$statistic^2 / sqrt(t1$parameter), 2), nsmall=2)
##       )

## paste(sep='', 't(',
##       round(t2$parameter), ') = ',
##       format(round(t2$statistic, 2), nsmall=2), ', p = ',
##       format(round(t2$p.value, 2), nsmall=2), ', d = ',
##       format(round(t2$statistic^2 / sqrt(t2$parameter), 2), nsmall=2)
##       )

## paste(sep='', 't(',
##       round(t3$parameter), ') = ',
##       format(round(t3$statistic, 2), nsmall=2), ', p = ',
##       format(round(t3$p.value, 2), nsmall=2), ', d = ',
##       format(round(t3$statistic^2 / sqrt(t3$parameter), 2), nsmall=2)
##       )
