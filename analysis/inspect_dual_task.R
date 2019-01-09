## NOTE: mean dual-task accuracy box plot
dd <- d[!(cndname%in%c("N-RB", "N-II")), dtacc[1], .(cndname, sub)]
ggplot(dd, aes(cndname, V1)) +
  geom_boxplot() +
  geom_point(alpha=0.5) +
  ## geom_hline(yintercept=dtaccthresh, colour='red', linetype="dashed") +
  ylab('Mean Dual-Task Accuracy') +
  xlab('Condition') +
  theme_classic() +
  theme(aspect.ratio = 1) +
  theme(strip.background = element_blank())
ggsave("../figs/dt_accuracy_box.pdf")

## NOTE: mean dual-task accuracy bar plot
dd <- d[!(cndname%in%c("N-RB", "N-II")), dtacc[1], .(cndname, sub)]
ddd <- dd[, .(mean(V1, na.rm=TRUE), sd(V1, na.rm=TRUE)/sqrt(.N)), .(cndname)]
ggplot(ddd, aes(cndname, V1)) +
  geom_bar(stat="identity", colour="black", fill="white", width=0.8) +
  geom_errorbar(aes(ymin=V1-V2, ymax=V1+V2), width=0.05) +
  ylab('Mean Dual-Task Accuracy') +
  xlab('Condition') +
  theme_classic() +
  theme(aspect.ratio = 1) +
  theme(strip.background = element_blank())
ggsave("../figs/dt_accuracy_bar.pdf")

## NOTE: Is the mean dual-task accuracy different across conditions?
anova(lm(V1~cndname, data=dd))

## NOTE: Correlation between dual-task and category learning?
dd <- d[!(cndname%in%c("N-RB", "N-II")),
        .(mean(acc, na.rm=TRUE), mean(dtacc, na.rm=TRUE)),
        .(cndname, sub)]

ggplot(dd, aes(V1, V2, colour=cndname)) +
  geom_point() +
  geom_smooth(method="lm") +
  facet_wrap(~cndname) +
  xlab('Mean Dual-Task Accuracy') +
  ylab('Mean Classification Accuracy') +
  theme_classic() +
  theme(aspect.ratio = 1) +
  theme(strip.background = element_blank())
ggsave("../figs/class_dt_corr.pdf")

## NOTE: exclusion figure --- dual-task
Nexclude <- d[dtacc < dtaccthresh, unique(sub), .(cndname)][, .N, .(cndname)]
Ntotal <- d[, unique(sub), .(cndname)][, .N, .(cndname)]

Nexclude[, Participants := 'Excluded']
Ntotal[, Participants := 'total']

dd <- rbindlist(list(Nexclude, Ntotal))

ggplot(dd[!(cndname%in%c("N-RB", "N-II"))],
       aes(cndname, N, fill=Participants)) +
  geom_bar(stat='identity', position=position_dodge(), colour="black") +
  ylab('Number of Participants') +
  xlab('Condition') +
  theme_classic() +
  theme(aspect.ratio = 1) +
  theme(strip.background = element_blank())
ggsave("../figs/dt_exc.pdf")

## ## NOTE: prop.test --- different number of exclusions per condition?
## x <- dd[Participants=='Excluded', N]
## n <- dd[Participants=='total', N]
## prop.test(x, n)
