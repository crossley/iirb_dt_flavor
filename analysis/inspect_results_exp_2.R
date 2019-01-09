library('data.table')
library('ggplot2')
library('stringr')

rm( list = ls() )
dtaccthresh  <- 0.0
source('assemble_data.R')
source('inspect_gender.R')
source('inspect_date.R')
source('inspect_dual_task.R')
source('exclude_ppts.R')
source('inspect_learning_curve.R')
source('inspect_button_switch.R')

rm( list = ls() )
source('assemble_data.R')
source('inspect_exclude.R')

## TODO:
## decision bound models?
## Reaction times and number of "too slows?"
## date-time confound?
