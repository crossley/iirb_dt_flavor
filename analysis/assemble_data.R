fnames1 <- list.files(
  '../Data/EXP3 - 2back Dual Task',
  pattern='.csv',
  full.names=TRUE,
  recursive=TRUE)

fnames2 <- list.files(
    '../Data/EXP1_Data/',
    pattern='.csv',
    full.names=TRUE,
    recursive=TRUE)

ldf1 <- lapply(
  fnames1,
  function(z) { z<-fread(z) })

ldf1 <- lapply(
  seq_along(ldf1),
  function(z) {
    ldf1[[z]][, sub := as.numeric(
                 unlist(str_extract_all(fnames1[z], "[0-9]+")))[5]]
  })

ldf2 <- lapply(
    fnames2,
    function(z) { z<-fread(z) })

ldf2 <- lapply(
    seq_along(ldf2),
    function(z) {
        ldf2[[z]][, sub := as.numeric(
                       unlist(str_extract_all(fnames2[z], "[0-9]+")))[4]]
    })

d1 <- rbindlist(ldf1, fill=TRUE)
d2 <- rbindlist(ldf2, fill=TRUE)

setnames(d1, "Key pressed", "key_pressed")
setnames(d1, "Correct?", "correct")
setnames(d1, "Block Number", "block")
setnames(d1, 'Int Correct?', 'intCorrect')

setnames(d2, "Key pressed", "key_pressed")
setnames(d2, "Correct?", "correct")
setnames(d2, "Block Number", "block")

d1[, acc := as.numeric(key_pressed == Category)]
d2[, acc := as.numeric(key_pressed == Category)]

d1[, dtacc := mean(intCorrect == "Y"), .(sub)]

d11 <- d1[, .(block, acc, gender, sub, dtacc)]
d22 <- d2[, .(block, acc, gender, sub)]
d22[, dtacc := NA]

d <- rbindlist(list(d11, d22))

cndname <- c("V-RB", "V-RB", "V-RB", "V-RB", "V-RB", "V-RB", "V-RB", "V-RB",
             "V-RB", "V-RB", "V-RB", "V-RB", "V-RB", "V-RB", "V-RB", "V-RB",
             "V-RB", "V-RB", "V-RB", "S-RB", "S-RB", "S-RB", "S-RB", "S-RB",
             "S-RB", "S-RB", "S-RB", "S-RB", "S-RB", "S-RB", "S-RB", "S-RB",
             "S-RB", "S-RB", "S-RB", "S-RB", "S-RB", "S-RB", "S-RB", "S-RB",
             "S-RB", "S-RB", "S-RB", "S-RB", "V-RB", "V-RB", "V-RB", "V-RB",
             "V-RB", "V-RB", "V-RB", "V-RB", "V-RB", "V-RB", "V-RB", "V-RB",
             "V-RB", "V-RB", "V-RB", "V-RB", "V-RB", "S-RB", "S-II", "S-II",
             "S-II", "S-II", "S-II", "S-II", "S-II", "S-II", "S-II", "S-II",
             "S-II", "V-II", "V-II", "V-II", "V-II", "V-II", "V-II", "V-II",
             "V-II", "V-II", "V-RB", "S-II", "S-II", "V-II", "V-II", "S-II",
             "S-II", "S-II", "V-II", "V-II", "S-II", "S-II", "V-II", "V-II",
             "V-II", "V-II", "V-II", "V-II", "V-II", "V-II", "S-II", "S-II",
             "S-II", rep("S-II", length(822:826)))

rbii <- c("RB", "RB", "RB", "RB", "RB", "RB", "RB", "RB", "RB", "RB", "RB",
          "RB", "RB", "RB", "RB", "RB", "RB", "RB", "RB", "RB", "RB", "RB",
          "RB", "RB", "RB", "RB", "RB", "RB", "RB", "RB", "RB", "RB", "RB",
          "RB", "RB", "RB", "RB", "RB", "RB", "RB", "RB", "RB", "RB", "RB",
          "RB", "RB", "RB", "RB", "RB", "RB", "RB", "RB", "RB", "RB", "RB",
          "RB", "RB", "RB", "RB", "RB", "RB", "RB", "II", "II", "II", "II",
          "II", "II", "II", "II", "II", "II", "II", "II", "II", "II", "II",
          "II", "II", "II", "II", "II", "RB", "II", "II", "II", "II", "II",
          "II", "II", "II", "II", "II", "II", "II", "II", "II", "II", "II",
          "II", "II", "II", "II", "II", "II", rep("II", length(822:826)))

condition <- c("V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V",
               "V", "V", "V", "V", "V", "V", "S", "S", "S", "S", "S", "S", "S",
               "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S",
               "S", "S", "S", "S", "S", "V", "V", "V", "V", "V", "V", "V", "V",
               "V", "V", "V", "V", "V", "V", "V", "V", "V", "S", "S", "S", "S",
               "S", "S", "S", "S", "S", "S", "S", "S", "V", "V", "V", "V", "V",
               "V", "V", "V", "V", "V", "S", "S", "V", "V", "S", "S", "S", "V",
               "V", "S", "S", "V", "V", "V", "V", "V", "V", "V", "V", "S", "S",
               "S", rep("S", length(822:826)))

sub <- c(601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 615,
         616, 617, 618, 619, 620, 624, 625, 626, 627, 628, 629, 630, 631, 632,
         633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646,
         647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660,
         661, 662, 663, 664, 665, 666, 701, 702, 703, 704, 705, 706, 707, 708,
         709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 722, 800,
         801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814,
         815, 816, 817, 818, 819, 820, 821, 822:826)

subRB <- c(110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123,
           124, 125, 126, 127, 128, 129, 130, 131, 132)

subII <- c(201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214,
           215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225)

cndname <- c(cndname, rep("N-RB", length(subRB)))
cndname <- c(cndname, rep("N-II", length(subII)))
sub <- c(sub, subRB, subII)
condition <- c(condition, rep("N", length(subRB)+length(subII)))
rbii <- c(rbii, rep("RB", length(subRB)))
rbii <- c(rbii, rep("II", length(subII)))

dts <- data.table(sub, rbii, condition, cndname)
d <- merge(d, dts, all=TRUE)
d <- d[!is.na(rbii)]
d <- d[!is.na(block)]
d[block %in% c(11,12), acc := 1-acc]

d[, npercnd := length(unique(sub)), .(cndname)]
