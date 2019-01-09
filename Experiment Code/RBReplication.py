from psychopy import visual, core, event, data, gui, sound #import some libraries from PsychoPy

#get info about experiment
dialogue=gui.Dlg(title="Experiment Information")
#subject info
dialogue.addText('Subject Information')
dialogue.addField('Subject ID:')
dialogue.addField('Gender:')
dialogue.addField('Age:')
dialogue.show()

#create a window with black background, full screen, pixels
win = visual.Window(size=(800, 600), fullscr=True, color=[-1,-1,-1], monitor="testMonitor", units='pix')

if dialogue.OK: #experiment info collected successfully
    exp_info=dialogue.data
    subject_ID=exp_info[0]
    gender=exp_info[1]
    age=exp_info[2]
   
    #create experiment handler
    experiment=data.ExperimentHandler(name='subject '+subject_ID,
             extraInfo={'gender':gender,
                        'age':age},
             dataFileName='subject'+subject_ID)
             
    #let participant know experiment is beginning
    instr1=visual.TextStim(win,text='In this experiment you will be looking at various stimuli, and learning which category each stimulus belongs to. There are two categories, and each category is equally likely. Perfect performance is possible.', color=[1,1,1], height=40, wrapWidth=1000)
    space=visual.TextStim(win, text='Press any key to continue', color=[1,1,1], pos=(0, -300))
    instr1.draw()
    space.draw()
    win.flip()
    event.waitKeys()
    
    instr2=visual.TextStim(win,text='We will begin with 10 rounds of training. Please use your index fingers to press the keys to indicate which category each stimuli belongs to. After the 10th round, the response buttons with switch. You will be informed of the switch immediately before the switch occurs.', color=[1,1,1], height=40, wrapWidth=1000)
    instr2.draw()
    space.draw()
    win.flip()
    event.waitKeys()
    
    any_qs=visual.TextStim(win,text='At this time, please ask your experimenter any questions you may have. Otherwise, press any key to continue.', color=[1,1,1], height=40, wrapWidth=1000)
    any_qs.draw()
    win.flip()
    q_key = event.waitKeys(timeStamped=True)
    
    start_text=visual.TextStim(win,text='The experiment will now automatically begin. Please place your index fingers on the colored keys.', color=[1,1,1], height=40, wrapWidth=900)
    start_text.draw()
    win.flip()
    core.wait(3)
   
    #depository of pre-set lines here
    
    lines=[visual.Line(win,start=(139.5,0), end=(-139.5,0), ori=-138),
           visual.Line(win,start=(157,0), end=(-157,0), ori=-139),
           visual.Line(win,start=(174,0), end=(-174,0), ori=-68),
           visual.Line(win,start=(170.5,0), end=(-170.5,0), ori=-84),
           visual.Line(win,start=(138,0), end=(-138,0), ori=-88),
           visual.Line(win,start=(171,0), end=(-171,0), ori=-90),
           visual.Line(win,start=(156.5,0), end=(-156.5,0), ori=-162),
           visual.Line(win,start=(160,0), end=(-160,0), ori=-118),
           visual.Line(win,start=(160.5,0), end=(-160.5,0), ori=-130),
           visual.Line(win,start=(174.5,0), end=(-174.5,0), ori=-87),
           visual.Line(win,start=(144.5,0), end=(-144.5,0), ori=-33),
           visual.Line(win,start=(162.5,0), end=(-162.5,0), ori=-161),
           visual.Line(win,start=(159.5,0), end=(-159.5,0), ori=-108),
           visual.Line(win,start=(145.5,0), end=(-145.5,0), ori=-95),
           visual.Line(win,start=(145.5,0), end=(-145.5,0), ori=-91),
           visual.Line(win,start=(151.5,0), end=(-151.5,0), ori=-94),
           visual.Line(win,start=(157.5,0), end=(-157.5,0), ori=-65),
           visual.Line(win,start=(160.5,0), end=(-160.5,0), ori=-128),
           visual.Line(win,start=(160,0), end=(-160,0), ori=-76),
           visual.Line(win,start=(138,0), end=(-138,0), ori=-26),
           visual.Line(win,start=(139,0), end=(-139,0), ori=-50),
           visual.Line(win,start=(170.5,0), end=(-170.5,0), ori=-112),
           visual.Line(win,start=(163.5,0), end=(-163.5,0), ori=-90),
           visual.Line(win,start=(142,0), end=(-142,0), ori=-149),
           visual.Line(win,start=(156,0), end=(-156,0), ori=-26),
           visual.Line(win,start=(167,0), end=(-167,0), ori=-81),
           visual.Line(win,start=(144.5,0), end=(-144.5,0), ori=-161),
           visual.Line(win,start=(167,0), end=(-167,0), ori=-66),
           visual.Line(win,start=(151,0), end=(-151,0), ori=-165),
           visual.Line(win,start=(160.5,0), end=(-160.5,0), ori=-142),
           visual.Line(win,start=(147.5,0), end=(-147.5,0), ori=-134),
           visual.Line(win,start=(169.5,0), end=(-169.5,0), ori=-86),
           visual.Line(win,start=(152.5,0), end=(-152.5,0), ori=-133),
           visual.Line(win,start=(143,0), end=(-143,0), ori=-104),
           visual.Line(win,start=(169.5,0), end=(-169.5,0), ori=-68),
           visual.Line(win,start=(147,0), end=(-147,0), ori=-84),
           visual.Line(win,start=(170.5,0), end=(-170.5,0), ori=-171),
           visual.Line(win,start=(145.5,0), end=(-145.5,0), ori=-143),
           visual.Line(win,start=(152.5,0), end=(-152.5,0), ori=-113),
           visual.Line(win,start=(170,0), end=(-170,0), ori=-38),
           visual.Line(win,start=(166,0), end=(-166,0), ori=-67),
           visual.Line(win,start=(163,0), end=(-163,0), ori=-138),
           visual.Line(win,start=(149,0), end=(-149,0), ori=-152),
           visual.Line(win,start=(170.5,0), end=(-170.5,0), ori=-50),
           visual.Line(win,start=(174.5,0), end=(-174.5,0), ori=-89),
           visual.Line(win,start=(144,0), end=(-144,0), ori=-74),
           visual.Line(win,start=(164,0), end=(-164,0), ori=-167),
           visual.Line(win,start=(146,0), end=(-146,0), ori=-75),
           visual.Line(win,start=(160,0), end=(-160,0), ori=-59),
           visual.Line(win,start=(140,0), end=(-140,0), ori=-160),
           visual.Line(win,start=(139.5,0), end=(-139.5,0), ori=-123),
           visual.Line(win,start=(168.5,0), end=(-168.5,0), ori=-74),
           visual.Line(win,start=(154,0), end=(-154,0), ori=-124),
           visual.Line(win,start=(149.5,0), end=(-149.5,0), ori=-99),
           visual.Line(win,start=(150.5,0), end=(-150.5,0), ori=-59),
           visual.Line(win,start=(149,0), end=(-149,0), ori=-127),
           visual.Line(win,start=(152,0), end=(-152,0), ori=-38),
           visual.Line(win,start=(160.5,0), end=(-160.5,0), ori=-163),
           visual.Line(win,start=(157.5,0), end=(-157.5,0), ori=-43),
           visual.Line(win,start=(137.5,0), end=(-137.5,0), ori=-137),
           visual.Line(win,start=(173,0), end=(-173,0), ori=-111),
           visual.Line(win,start=(163,0), end=(-163,0), ori=-100),
           visual.Line(win,start=(156,0), end=(-156,0), ori=-58),
           visual.Line(win,start=(155,0), end=(-155,0), ori=-160),
           visual.Line(win,start=(167,0), end=(-167,0), ori=-115),
           visual.Line(win,start=(156,0), end=(-156,0), ori=-164),
           visual.Line(win,start=(150,0), end=(-150,0), ori=-122),
           visual.Line(win,start=(157.5,0), end=(-157.5,0), ori=-154),
           visual.Line(win,start=(146.5,0), end=(-146.5,0), ori=-145),
           visual.Line(win,start=(145.5,0), end=(-145.5,0), ori=-119),
           visual.Line(win,start=(139.5,0), end=(-139.5,0), ori=-170),
           visual.Line(win,start=(152.5,0), end=(-152.5,0), ori=-46),
           visual.Line(win,start=(170.5,0), end=(-170.5,0), ori=-91),
           visual.Line(win,start=(147.5,0), end=(-147.5,0), ori=-172),
           visual.Line(win,start=(164.5,0), end=(-164.5,0), ori=-167),
           visual.Line(win,start=(158,0), end=(-158,0), ori=-105),
           visual.Line(win,start=(149.5,0), end=(-149.5,0), ori=-133),
           visual.Line(win,start=(139,0), end=(-139,0), ori=-42),
           visual.Line(win,start=(170.5,0), end=(-170.5,0), ori=-31),
           visual.Line(win,start=(173.5,0), end=(-173.5,0), ori=-149),
           visual.Line(win,start=(139,0), end=(-139,0), ori=-123),
           visual.Line(win,start=(170,0), end=(-170,0), ori=-29),
           visual.Line(win,start=(164,0), end=(-164,0), ori=-149),
           visual.Line(win,start=(174.5,0), end=(-174.5,0), ori=-63),
           visual.Line(win,start=(160,0), end=(-160,0), ori=-93),
           visual.Line(win,start=(173,0), end=(-173,0), ori=-28),
           visual.Line(win,start=(154.5,0), end=(-154.5,0), ori=-38),
           visual.Line(win,start=(150,0), end=(-150,0), ori=-82),
           visual.Line(win,start=(164.5,0), end=(-164.5,0), ori=-133),
           visual.Line(win,start=(162.5,0), end=(-162.5,0), ori=-38),
           visual.Line(win,start=(139,0), end=(-139,0), ori=-155),
           visual.Line(win,start=(161,0), end=(-161,0), ori=-107),
           visual.Line(win,start=(148.5,0), end=(-148.5,0), ori=-112),
           visual.Line(win,start=(171.5,0), end=(-171.5,0), ori=-89),
           visual.Line(win,start=(159.5,0), end=(-159.5,0), ori=-61),
           visual.Line(win,start=(173,0), end=(-173,0), ori=-164),
           visual.Line(win,start=(158,0), end=(-158,0), ori=-144),
           visual.Line(win,start=(168,0), end=(-168,0), ori=-145),
           visual.Line(win,start=(144,0), end=(-144,0), ori=-104),
           visual.Line(win,start=(139.5,0), end=(-139.5,0), ori=-119),
           visual.Line(win,start=(139.5,0), end=(-139.5,0), ori=-69),
           visual.Line(win,start=(155,0), end=(-155,0), ori=-79),
           visual.Line(win,start=(154,0), end=(-154,0), ori=-53),
           visual.Line(win,start=(166.5,0), end=(-166.5,0), ori=-162),
           visual.Line(win,start=(169.5,0), end=(-169.5,0), ori=-172),
           visual.Line(win,start=(163,0), end=(-163,0), ori=-74),
           visual.Line(win,start=(139.5,0), end=(-139.5,0), ori=-74),
           visual.Line(win,start=(148.5,0), end=(-148.5,0), ori=-104),
           visual.Line(win,start=(141,0), end=(-141,0), ori=-38),
           visual.Line(win,start=(153,0), end=(-153,0), ori=-116),
           visual.Line(win,start=(167,0), end=(-167,0), ori=-126),
           visual.Line(win,start=(156.5,0), end=(-156.5,0), ori=-90),
           visual.Line(win,start=(161.5,0), end=(-161.5,0), ori=-142),
           visual.Line(win,start=(156,0), end=(-156,0), ori=-72),
           visual.Line(win,start=(149,0), end=(-149,0), ori=-94),
           visual.Line(win,start=(141,0), end=(-141,0), ori=-97),
           visual.Line(win,start=(145.5,0), end=(-145.5,0), ori=-115),
           visual.Line(win,start=(142,0), end=(-142,0), ori=-145),
           visual.Line(win,start=(158,0), end=(-158,0), ori=-99),
           visual.Line(win,start=(163,0), end=(-163,0), ori=-152),
           visual.Line(win,start=(156.5,0), end=(-156.5,0), ori=-46),
           visual.Line(win,start=(168.5,0), end=(-168.5,0), ori=-82),
           visual.Line(win,start=(167.5,0), end=(-167.5,0), ori=-55),
           visual.Line(win,start=(145.5,0), end=(-145.5,0), ori=-64),
           visual.Line(win,start=(174.5,0), end=(-174.5,0), ori=-98),
           visual.Line(win,start=(149,0), end=(-149,0), ori=-115),
           visual.Line(win,start=(156.5,0), end=(-156.5,0), ori=-100),
           visual.Line(win,start=(145.5,0), end=(-145.5,0), ori=-102),
           visual.Line(win,start=(157.5,0), end=(-157.5,0), ori=-84),
           visual.Line(win,start=(150.5,0), end=(-150.5,0), ori=-28),
           visual.Line(win,start=(154.5,0), end=(-154.5,0), ori=-33),
           visual.Line(win,start=(157.5,0), end=(-157.5,0), ori=-68),
           visual.Line(win,start=(147,0), end=(-147,0), ori=-53),
           visual.Line(win,start=(160.5,0), end=(-160.5,0), ori=-167),
           visual.Line(win,start=(163.5,0), end=(-163.5,0), ori=-149),
           visual.Line(win,start=(162,0), end=(-162,0), ori=-73),
           visual.Line(win,start=(161.5,0), end=(-161.5,0), ori=-133),
           visual.Line(win,start=(169,0), end=(-169,0), ori=-37),
           visual.Line(win,start=(169.5,0), end=(-169.5,0), ori=-71),
           visual.Line(win,start=(155.5,0), end=(-155.5,0), ori=-172),
           visual.Line(win,start=(146,0), end=(-146,0), ori=-59),
           visual.Line(win,start=(174.5,0), end=(-174.5,0), ori=-169),
           visual.Line(win,start=(156,0), end=(-156,0), ori=-131),
           visual.Line(win,start=(173,0), end=(-173,0), ori=-165),
           visual.Line(win,start=(154.5,0), end=(-154.5,0), ori=-103),
           visual.Line(win,start=(141,0), end=(-141,0), ori=-108),
           visual.Line(win,start=(158.5,0), end=(-158.5,0), ori=-126),
           visual.Line(win,start=(159.5,0), end=(-159.5,0), ori=-69),
           visual.Line(win,start=(164.5,0), end=(-164.5,0), ori=-171),
           visual.Line(win,start=(166.5,0), end=(-166.5,0), ori=-29),
           visual.Line(win,start=(156.5,0), end=(-156.5,0), ori=-164),
           visual.Line(win,start=(144,0), end=(-144,0), ori=-25),
           visual.Line(win,start=(163.5,0), end=(-163.5,0), ori=-25),
           visual.Line(win,start=(146,0), end=(-146,0), ori=-71),
           visual.Line(win,start=(152.5,0), end=(-152.5,0), ori=-109),
           visual.Line(win,start=(172,0), end=(-172,0), ori=-144),
           visual.Line(win,start=(145.5,0), end=(-145.5,0), ori=-99),
           visual.Line(win,start=(171.5,0), end=(-171.5,0), ori=-141),
           visual.Line(win,start=(142.5,0), end=(-142.5,0), ori=-62),
           visual.Line(win,start=(161,0), end=(-161,0), ori=-91),
           visual.Line(win,start=(145.5,0), end=(-145.5,0), ori=-98),
           visual.Line(win,start=(152,0), end=(-152,0), ori=-122),
           visual.Line(win,start=(159.5,0), end=(-159.5,0), ori=-172),
           visual.Line(win,start=(157,0), end=(-157,0), ori=-120),
           visual.Line(win,start=(170.5,0), end=(-170.5,0), ori=-162),
           visual.Line(win,start=(165.5,0), end=(-165.5,0), ori=-64),
           visual.Line(win,start=(163.5,0), end=(-163.5,0), ori=-109),
           visual.Line(win,start=(173,0), end=(-173,0), ori=-172),
           visual.Line(win,start=(140.5,0), end=(-140.5,0), ori=-45),
           visual.Line(win,start=(163.5,0), end=(-163.5,0), ori=-73),
           visual.Line(win,start=(153,0), end=(-153,0), ori=-51),
           visual.Line(win,start=(174,0), end=(-174,0), ori=-164),
           visual.Line(win,start=(175,0), end=(-175,0), ori=-128),
           visual.Line(win,start=(172,0), end=(-172,0), ori=-30),
           visual.Line(win,start=(139,0), end=(-139,0), ori=-77),
           visual.Line(win,start=(159,0), end=(-159,0), ori=-151),
           visual.Line(win,start=(143.5,0), end=(-143.5,0), ori=-132),
           visual.Line(win,start=(143.5,0), end=(-143.5,0), ori=-51),
           visual.Line(win,start=(139,0), end=(-139,0), ori=-124),
           visual.Line(win,start=(168,0), end=(-168,0), ori=-32),
           visual.Line(win,start=(143.5,0), end=(-143.5,0), ori=-106),
           visual.Line(win,start=(172.5,0), end=(-172.5,0), ori=-43),
           visual.Line(win,start=(151.5,0), end=(-151.5,0), ori=-59),
           visual.Line(win,start=(151.5,0), end=(-151.5,0), ori=-163),
           visual.Line(win,start=(160.5,0), end=(-160.5,0), ori=-49),
           visual.Line(win,start=(172,0), end=(-172,0), ori=-99),
           visual.Line(win,start=(159,0), end=(-159,0), ori=-52),
           visual.Line(win,start=(171.5,0), end=(-171.5,0), ori=-109),
           visual.Line(win,start=(171.5,0), end=(-171.5,0), ori=-133),
           visual.Line(win,start=(145,0), end=(-145,0), ori=-159),
           visual.Line(win,start=(166,0), end=(-166,0), ori=-30),
           visual.Line(win,start=(144,0), end=(-144,0), ori=-54),
           visual.Line(win,start=(154,0), end=(-154,0), ori=-129),
           visual.Line(win,start=(162.5,0), end=(-162.5,0), ori=-110),
           visual.Line(win,start=(168,0), end=(-168,0), ori=-40),
           visual.Line(win,start=(154,0), end=(-154,0), ori=-154),
           visual.Line(win,start=(169.5,0), end=(-169.5,0), ori=-42),
           visual.Line(win,start=(172,0), end=(-172,0), ori=-135),
           visual.Line(win,start=(159,0), end=(-159,0), ori=-86),
           visual.Line(win,start=(159.5,0), end=(-159.5,0), ori=-123),
           visual.Line(win,start=(150,0), end=(-150,0), ori=-159),
           visual.Line(win,start=(156.5,0), end=(-156.5,0), ori=-35),
           visual.Line(win,start=(161,0), end=(-161,0), ori=-133),
           visual.Line(win,start=(139,0), end=(-139,0), ori=-131),
           visual.Line(win,start=(159,0), end=(-159,0), ori=-155),
           visual.Line(win,start=(137.5,0), end=(-137.5,0), ori=-164),
           visual.Line(win,start=(147,0), end=(-147,0), ori=-81),
           visual.Line(win,start=(146.5,0), end=(-146.5,0), ori=-30),
           visual.Line(win,start=(171.5,0), end=(-171.5,0), ori=-77),
           visual.Line(win,start=(141,0), end=(-141,0), ori=-114),
           visual.Line(win,start=(147,0), end=(-147,0), ori=-66),
           visual.Line(win,start=(167,0), end=(-167,0), ori=-165),
           visual.Line(win,start=(166.5,0), end=(-166.5,0), ori=-103),
           visual.Line(win,start=(155.5,0), end=(-155.5,0), ori=-113),
           visual.Line(win,start=(173.5,0), end=(-173.5,0), ori=-174),
           visual.Line(win,start=(163.5,0), end=(-163.5,0), ori=-78),
           visual.Line(win,start=(163,0), end=(-163,0), ori=-42),
           visual.Line(win,start=(161,0), end=(-161,0), ori=-39),
           visual.Line(win,start=(174.5,0), end=(-174.5,0), ori=-95),
           visual.Line(win,start=(157.5,0), end=(-157.5,0), ori=-168),
           visual.Line(win,start=(139.5,0), end=(-139.5,0), ori=-137),
           visual.Line(win,start=(147,0), end=(-147,0), ori=-123),
           visual.Line(win,start=(137.5,0), end=(-137.5,0), ori=-151),
           visual.Line(win,start=(154,0), end=(-154,0), ori=-129),
           visual.Line(win,start=(171.5,0), end=(-171.5,0), ori=-127),
           visual.Line(win,start=(171.5,0), end=(-171.5,0), ori=-78),
           visual.Line(win,start=(149.5,0), end=(-149.5,0), ori=-64),
           visual.Line(win,start=(140,0), end=(-140,0), ori=-140),
           visual.Line(win,start=(140.5,0), end=(-140.5,0), ori=-29),
           visual.Line(win,start=(171.5,0), end=(-171.5,0), ori=-161),
           visual.Line(win,start=(158,0), end=(-158,0), ori=-127),
           visual.Line(win,start=(173,0), end=(-173,0), ori=-156),
           visual.Line(win,start=(159.5,0), end=(-159.5,0), ori=-133),
           visual.Line(win,start=(159.5,0), end=(-159.5,0), ori=-51),
           visual.Line(win,start=(141,0), end=(-141,0), ori=-105),
           visual.Line(win,start=(146.5,0), end=(-146.5,0), ori=-139),
           visual.Line(win,start=(143.5,0), end=(-143.5,0), ori=-125),
           visual.Line(win,start=(155.5,0), end=(-155.5,0), ori=-93),
           visual.Line(win,start=(162.5,0), end=(-162.5,0), ori=-47),
           visual.Line(win,start=(154.5,0), end=(-154.5,0), ori=-86),
           visual.Line(win,start=(142.5,0), end=(-142.5,0), ori=-30),
           visual.Line(win,start=(154.5,0), end=(-154.5,0), ori=-64),
           visual.Line(win,start=(149.5,0), end=(-149.5,0), ori=-26),
           visual.Line(win,start=(137.5,0), end=(-137.5,0), ori=-115),
           visual.Line(win,start=(142,0), end=(-142,0), ori=-56),
           visual.Line(win,start=(160.5,0), end=(-160.5,0), ori=-149),
           visual.Line(win,start=(144.5,0), end=(-144.5,0), ori=-56),
           visual.Line(win,start=(152,0), end=(-152,0), ori=-99),
           visual.Line(win,start=(142.5,0), end=(-142.5,0), ori=-103),
           visual.Line(win,start=(166,0), end=(-166,0), ori=-85),
           visual.Line(win,start=(138.5,0), end=(-138.5,0), ori=-31),
           visual.Line(win,start=(170,0), end=(-170,0), ori=-123),
           visual.Line(win,start=(171,0), end=(-171,0), ori=-111),
           visual.Line(win,start=(169,0), end=(-169,0), ori=-58),
           visual.Line(win,start=(147.5,0), end=(-147.5,0), ori=-36),
           visual.Line(win,start=(167,0), end=(-167,0), ori=-52),
           visual.Line(win,start=(151,0), end=(-151,0), ori=-162),
           visual.Line(win,start=(142.5,0), end=(-142.5,0), ori=-27),
           visual.Line(win,start=(165,0), end=(-165,0), ori=-64),
           visual.Line(win,start=(172.5,0), end=(-172.5,0), ori=-27),
           visual.Line(win,start=(139.5,0), end=(-139.5,0), ori=-138),
           visual.Line(win,start=(172.5,0), end=(-172.5,0), ori=-93),
           visual.Line(win,start=(172,0), end=(-172,0), ori=-102),
           visual.Line(win,start=(170.5,0), end=(-170.5,0), ori=-160),
           visual.Line(win,start=(141,0), end=(-141,0), ori=-140),
           visual.Line(win,start=(151,0), end=(-151,0), ori=-82),
           visual.Line(win,start=(156,0), end=(-156,0), ori=-45),
           visual.Line(win,start=(163,0), end=(-163,0), ori=-171),
           visual.Line(win,start=(156,0), end=(-156,0), ori=-130),
           visual.Line(win,start=(169,0), end=(-169,0), ori=-101),
           visual.Line(win,start=(145,0), end=(-145,0), ori=-30),
           visual.Line(win,start=(147.5,0), end=(-147.5,0), ori=-66),
           visual.Line(win,start=(157,0), end=(-157,0), ori=-34),
           visual.Line(win,start=(173,0), end=(-173,0), ori=-62),
           visual.Line(win,start=(162,0), end=(-162,0), ori=-139),
           visual.Line(win,start=(150.5,0), end=(-150.5,0), ori=-71),
           visual.Line(win,start=(141.5,0), end=(-141.5,0), ori=-139),
           visual.Line(win,start=(162,0), end=(-162,0), ori=-136),
           visual.Line(win,start=(163,0), end=(-163,0), ori=-158),
           visual.Line(win,start=(155,0), end=(-155,0), ori=-172),
           visual.Line(win,start=(169,0), end=(-169,0), ori=-116),
           visual.Line(win,start=(140,0), end=(-140,0), ori=-94),
           visual.Line(win,start=(153,0), end=(-153,0), ori=-114),
           visual.Line(win,start=(165,0), end=(-165,0), ori=-53),
           visual.Line(win,start=(175,0), end=(-175,0), ori=-161),
           visual.Line(win,start=(148,0), end=(-148,0), ori=-57),
           visual.Line(win,start=(165,0), end=(-165,0), ori=-112),
           visual.Line(win,start=(153,0), end=(-153,0), ori=-62),
           visual.Line(win,start=(171.5,0), end=(-171.5,0), ori=-38),
           visual.Line(win,start=(150.5,0), end=(-150.5,0), ori=-161),
           visual.Line(win,start=(146.5,0), end=(-146.5,0), ori=-44),
           visual.Line(win,start=(148.5,0), end=(-148.5,0), ori=-161),
           visual.Line(win,start=(148.5,0), end=(-148.5,0), ori=-173),
           visual.Line(win,start=(142,0), end=(-142,0), ori=-40),
           visual.Line(win,start=(159.5,0), end=(-159.5,0), ori=-55),
           visual.Line(win,start=(157,0), end=(-157,0), ori=-146),
           visual.Line(win,start=(144.5,0), end=(-144.5,0), ori=-44),
           visual.Line(win,start=(156,0), end=(-156,0), ori=-91),
           visual.Line(win,start=(164,0), end=(-164,0), ori=-43),
           visual.Line(win,start=(171.5,0), end=(-171.5,0), ori=-160),
           visual.Line(win,start=(228.5,0), end=(-228.5,0), ori=-138),#cat B
           visual.Line(win,start=(226,0), end=(-226,0), ori=-139),
           visual.Line(win,start=(228.5,0), end=(-228.5,0), ori=-68),
           visual.Line(win,start=(205.5,0), end=(-205.5,0), ori=-84),
           visual.Line(win,start=(202.5,0), end=(-202.5,0), ori=-88),
           visual.Line(win,start=(217.5,0), end=(-217.5,0), ori=-90),
           visual.Line(win,start=(206.5,0), end=(-206.5,0), ori=-162),
           visual.Line(win,start=(229.5,0), end=(-229.5,0), ori=-118),
           visual.Line(win,start=(222.5,0), end=(-222,0), ori=-130),
           visual.Line(win,start=(216.5,0), end=(-216.5,0), ori=-87),
           visual.Line(win,start=(221.5,0), end=(-221.5,0), ori=-33),
           visual.Line(win,start=(208.5,0), end=(-208.5,0), ori=-161),
           visual.Line(win,start=(206,0), end=(-206,0), ori=-108),
           visual.Line(win,start=(211.5,0), end=(-211.5,0), ori=-95),
           visual.Line(win,start=(225.5,0), end=(-225.5,0), ori=-91),
           visual.Line(win,start=(218,0), end=(-218,0), ori=-94),
           visual.Line(win,start=(224.5,0), end=(-224.5,0), ori=-65),
           visual.Line(win,start=(224,0), end=(-224,0), ori=-128),
           visual.Line(win,start=(217.5,0), end=(-217.5,0), ori=-76),
           visual.Line(win,start=(227.5,0), end=(-227.5,0), ori=-26),
           visual.Line(win,start=(207.5,0), end=(-207.5,0), ori=-50),
           visual.Line(win,start=(219,0), end=(-219,0), ori=-112),
           visual.Line(win,start=(214,0), end=(-214,0), ori=-90),
           visual.Line(win,start=(198.5,0), end=(-198.5,0), ori=-149),
           visual.Line(win,start=(215.5,0), end=(-215.5,0), ori=-26),
           visual.Line(win,start=(198.5,0), end=(-198.5,0), ori=-81),
           visual.Line(win,start=(206.5,0), end=(-206.5,0), ori=-161),
           visual.Line(win,start=(208,0), end=(-208,0), ori=-66),
           visual.Line(win,start=(228,0), end=(-228,0), ori=-165),
           visual.Line(win,start=(208.5,0), end=(-208.5,0), ori=-142),
           visual.Line(win,start=(206,0), end=(-206,0), ori=-134),
           visual.Line(win,start=(213,0), end=(-213,0), ori=-86),
           visual.Line(win,start=(201,0), end=(-201,0), ori=-133),
           visual.Line(win,start=(217.5,0), end=(-217.5,0), ori=-104),
           visual.Line(win,start=(210.5,0), end=(-210.5,0), ori=-68),
           visual.Line(win,start=(208,0), end=(-208,0), ori=-84),
           visual.Line(win,start=(228,0), end=(-228,0), ori=-171),
           visual.Line(win,start=(204,0), end=(-204,0), ori=-143),
           visual.Line(win,start=(224.5,0), end=(-224.5,0), ori=-113),
           visual.Line(win,start=(213,0), end=(-213,0), ori=-38),
           visual.Line(win,start=(230,0), end=(-230,0), ori=-67),
           visual.Line(win,start=(198.5,0), end=(-198.5,0), ori=-138),
           visual.Line(win,start=(214,0), end=(-214,0), ori=-152),
           visual.Line(win,start=(198.5,0), end=(-198.5,0), ori=-50),
           visual.Line(win,start=(221.5,0), end=(-221.5,0), ori=-89),
           visual.Line(win,start=(203,0), end=(-203,0), ori=-74),
           visual.Line(win,start=(204,0), end=(-204,0), ori=-167),
           visual.Line(win,start=(212.5,0), end=(-212.5,0), ori=-75),
           visual.Line(win,start=(198,0), end=(-198,0), ori=-59),
           visual.Line(win,start=(203,0), end=(-203,0), ori=-160),
           visual.Line(win,start=(222.5,0), end=(-222.5,0), ori=-123),
           visual.Line(win,start=(210,0), end=(-210,0), ori=-74),
           visual.Line(win,start=(203.5,0), end=(-203.5,0), ori=-124),
           visual.Line(win,start=(228.5,0), end=(-228.5,0), ori=-99),
           visual.Line(win,start=(210.5,0), end=(-210.5,0), ori=-59),
           visual.Line(win,start=(212,0), end=(-212,0), ori=-127),
           visual.Line(win,start=(214,0), end=(-214,0), ori=-38),
           visual.Line(win,start=(206,0), end=(-206,0), ori=-163),
           visual.Line(win,start=(229,0), end=(-229,0), ori=-43),
           visual.Line(win,start=(200,0), end=(-200,0), ori=-137),
           visual.Line(win,start=(213,0), end=(-213,0), ori=-111),
           visual.Line(win,start=(218,0), end=(-218,0), ori=-100),
           visual.Line(win,start=(212.5,0), end=(-212.5,0), ori=-58),
           visual.Line(win,start=(225.5,0), end=(-225.5,0), ori=-160),
           visual.Line(win,start=(218,0), end=(-218,0), ori=-115),
           visual.Line(win,start=(226.5,0), end=(-226.5,0), ori=-164),
           visual.Line(win,start=(221,0), end=(-221,0), ori=-122),
           visual.Line(win,start=(212.5,0), end=(-212.5,0), ori=-154),
           visual.Line(win,start=(228,0), end=(-228,0), ori=-145),
           visual.Line(win,start=(202.5,0), end=(-202.5,0), ori=-119),
           visual.Line(win,start=(222.5,0), end=(-222.5,0), ori=-170),
           visual.Line(win,start=(225,0), end=(-225,0), ori=-46),
           visual.Line(win,start=(224.5,0), end=(-224.5,0), ori=-91),
           visual.Line(win,start=(199,0), end=(-199,0), ori=-172),
           visual.Line(win,start=(197.5,0), end=(-197.5,0), ori=-167),
           visual.Line(win,start=(220,0), end=(-220,0), ori=-105),
           visual.Line(win,start=(207,0), end=(-207,0), ori=-133),
           visual.Line(win,start=(198,0), end=(-198,0), ori=-42),
           visual.Line(win,start=(225.5,0), end=(-225.5,0), ori=-31),
           visual.Line(win,start=(204,0), end=(-204,0), ori=-149),
           visual.Line(win,start=(211,0), end=(-211,0), ori=-123),
           visual.Line(win,start=(226,0), end=(-226,0), ori=-29),
           visual.Line(win,start=(223.5,0), end=(-223.5,0), ori=-149),
           visual.Line(win,start=(223,0), end=(-223,0), ori=-63),
           visual.Line(win,start=(208,0), end=(-208,0), ori=-93),
           visual.Line(win,start=(205.5,0), end=(-205.5,0), ori=-28),
           visual.Line(win,start=(228.5,0), end=(-228.5,0), ori=-38),
           visual.Line(win,start=(228.5,0), end=(-228.5,0), ori=-82),
           visual.Line(win,start=(204.5,0), end=(-204.5,0), ori=-133),
           visual.Line(win,start=(204,0), end=(-204,0), ori=-38),
           visual.Line(win,start=(221.5,0), end=(-221.5,0), ori=-155),
           visual.Line(win,start=(200.5,0), end=(-200.5,0), ori=-107),
           visual.Line(win,start=(226,0), end=(-226,0), ori=-112),
           visual.Line(win,start=(213.5,0), end=(-213.5,0), ori=-89),
           visual.Line(win,start=(210.5,0), end=(-210.5,0), ori=-61),
           visual.Line(win,start=(223,0), end=(-223,0), ori=-164),
           visual.Line(win,start=(210.5,0), end=(-210.5,0), ori=-144),
           visual.Line(win,start=(199,0), end=(-199,0), ori=-145),
           visual.Line(win,start=(216.5,0), end=(-216.5,0), ori=-104),
           visual.Line(win,start=(223,0), end=(-223,0), ori=-119),
           visual.Line(win,start=(214,0), end=(-214,0), ori=-69),
           visual.Line(win,start=(226.5,0), end=(-226.5,0), ori=-79),
           visual.Line(win,start=(205.5,0), end=(-205.5,0), ori=-53),
           visual.Line(win,start=(199.5,0), end=(-199.5,0), ori=-162),
           visual.Line(win,start=(199.5,0), end=(-199.5,0), ori=-172),
           visual.Line(win,start=(209.5,0), end=(-209.5,0), ori=-74),
           visual.Line(win,start=(225,0), end=(-225,0), ori=-74),
           visual.Line(win,start=(219.5,0), end=(-219.5,0), ori=-104),
           visual.Line(win,start=(219,0), end=(-219,0), ori=-38),
           visual.Line(win,start=(204.5,0), end=(-204.5,0), ori=-116),
           visual.Line(win,start=(211.5,0), end=(-211.5,0), ori=-126),
           visual.Line(win,start=(223,0), end=(-223,0), ori=-90),
           visual.Line(win,start=(208,0), end=(-208,0), ori=-142),
           visual.Line(win,start=(219,0), end=(-219,0), ori=-72),
           visual.Line(win,start=(229.5,0), end=(-229.5,0), ori=-94),
           visual.Line(win,start=(227,0), end=(-227,0), ori=-97),
           visual.Line(win,start=(227.5,0), end=(-227.5,0), ori=-115),
           visual.Line(win,start=(203,0), end=(-203,0), ori=-145),
           visual.Line(win,start=(212.5,0), end=(-212.5,0), ori=-99),
           visual.Line(win,start=(216.5,0), end=(-216.5,0), ori=-152),
           visual.Line(win,start=(207.5,0), end=(-207.5,0), ori=-46),
           visual.Line(win,start=(222.5,0), end=(-222.5,0), ori=-82),
           visual.Line(win,start=(202.5,0), end=(-202.5,0), ori=-55),
           visual.Line(win,start=(208.5,0), end=(-208.5,0), ori=-64),
           visual.Line(win,start=(207.5,0), end=(-207.5,0), ori=-98),
           visual.Line(win,start=(219,0), end=(-219,0), ori=-115),
           visual.Line(win,start=(207.5,0), end=(-207.5,0), ori=-100),
           visual.Line(win,start=(226,0), end=(-226,0), ori=-102),
           visual.Line(win,start=(218,0), end=(-218,0), ori=-84),
           visual.Line(win,start=(211.5,0), end=(-211.5,0), ori=-28),
           visual.Line(win,start=(200,0), end=(-200,0), ori=-33),
           visual.Line(win,start=(214,0), end=(-214,0), ori=-68),
           visual.Line(win,start=(213,0), end=(-213,0), ori=-53),
           visual.Line(win,start=(201.5,0), end=(-201.5,0), ori=-167),
           visual.Line(win,start=(228,0), end=(-228,0), ori=-149),
           visual.Line(win,start=(216.5,0), end=(-216.5,0), ori=-73),
           visual.Line(win,start=(197.5,0), end=(-197.5,0), ori=-133),
           visual.Line(win,start=(220.5,0), end=(-220.5,0), ori=-37),
           visual.Line(win,start=(203,0), end=(-203,0), ori=-71),
           visual.Line(win,start=(209.5,0), end=(-209.5,0), ori=-172),
           visual.Line(win,start=(201.5,0), end=(-201.5,0), ori=-59),
           visual.Line(win,start=(223,0), end=(-223,0), ori=-169),
           visual.Line(win,start=(211.5,0), end=(-211.5,0), ori=-131),
           visual.Line(win,start=(206,0), end=(-206,0), ori=-165),
           visual.Line(win,start=(213.5,0), end=(-213.5,0), ori=-103),
           visual.Line(win,start=(211,0), end=(-211,0), ori=-108),
           visual.Line(win,start=(205.5,0), end=(-205.5,0), ori=-126),
           visual.Line(win,start=(223,0), end=(-223,0), ori=-69),
           visual.Line(win,start=(222,0), end=(-222,0), ori=-171),
           visual.Line(win,start=(203,0), end=(-203,0), ori=-29),
           visual.Line(win,start=(199,0), end=(-199,0), ori=-164),
           visual.Line(win,start=(226,0), end=(-226,0), ori=-25),
           visual.Line(win,start=(211.5,0), end=(-211.5,0), ori=-25),
           visual.Line(win,start=(222.5,0), end=(-222.5,0), ori=-71),
           visual.Line(win,start=(215,0), end=(-215,0), ori=-109),
           visual.Line(win,start=(214,0), end=(-214,0), ori=-144),
           visual.Line(win,start=(213.5,0), end=(-213.5,0), ori=-99),
           visual.Line(win,start=(227.5,0), end=(-227.5,0), ori=-141),
           visual.Line(win,start=(210.5,0), end=(-210.5,0), ori=-62),
           visual.Line(win,start=(227,0), end=(-227,0), ori=-91),
           visual.Line(win,start=(223.5,0), end=(-223.5,0), ori=-98),
           visual.Line(win,start=(220.5,0), end=(-220.5,0), ori=-122),
           visual.Line(win,start=(217,0), end=(-217,0), ori=-172),
           visual.Line(win,start=(210.5,0), end=(-210.5,0), ori=-120),
           visual.Line(win,start=(218,0), end=(-218,0), ori=-162),
           visual.Line(win,start=(205,0), end=(-205,0), ori=-64),
           visual.Line(win,start=(206.5,0), end=(-206.5,0), ori=-109),
           visual.Line(win,start=(220.5,0), end=(-220.5,0), ori=-172),
           visual.Line(win,start=(212,0), end=(-212,0), ori=-45),
           visual.Line(win,start=(200,0), end=(-200,0), ori=-73),
           visual.Line(win,start=(217.5,0), end=(-217.5,0), ori=-51),
           visual.Line(win,start=(213.5,0), end=(-213.5,0), ori=-164),
           visual.Line(win,start=(227.5,0), end=(-227.5,0), ori=-128),
           visual.Line(win,start=(215,0), end=(-215,0), ori=-30),
           visual.Line(win,start=(208,0), end=(-208,0), ori=-77),
           visual.Line(win,start=(198.5,0), end=(-198.5,0), ori=-151),
           visual.Line(win,start=(206.5,0), end=(-206.5,0), ori=-132),
           visual.Line(win,start=(229,0), end=(-229,0), ori=-51),
           visual.Line(win,start=(225.5,0), end=(-225.5,0), ori=-124),
           visual.Line(win,start=(206,0), end=(-206,0), ori=-32),
           visual.Line(win,start=(210,0), end=(-210,0), ori=-106),
           visual.Line(win,start=(208,0), end=(-208,0), ori=-43),
           visual.Line(win,start=(212.5,0), end=(-212.5,0), ori=-59),
           visual.Line(win,start=(198.5,0), end=(-198.5,0), ori=-163),
           visual.Line(win,start=(198.5,0), end=(-198.5,0), ori=-49),
           visual.Line(win,start=(201,0), end=(-201,0), ori=-99),
           visual.Line(win,start=(229,0), end=(-229,0), ori=-52),
           visual.Line(win,start=(201,0), end=(-201,0), ori=-109),
           visual.Line(win,start=(226,0), end=(-226,0), ori=-133),
           visual.Line(win,start=(209.5,0), end=(-209.5,0), ori=-159),
           visual.Line(win,start=(213.5,0), end=(-213.5,0), ori=-30),
           visual.Line(win,start=(226.5,0), end=(-226.5,0), ori=-54),
           visual.Line(win,start=(208.5,0), end=(-208.5,0), ori=-129),
           visual.Line(win,start=(226,0), end=(-226,0), ori=-110),
           visual.Line(win,start=(210.5,0), end=(-210.5,0), ori=-40),
           visual.Line(win,start=(206,0), end=(-206,0), ori=-154),
           visual.Line(win,start=(223.5,0), end=(-223.5,0), ori=-42),
           visual.Line(win,start=(205.5,0), end=(-205.5,0), ori=-135),
           visual.Line(win,start=(209,0), end=(-209,0), ori=-86),
           visual.Line(win,start=(208.5,0), end=(-208.5,0), ori=-123),
           visual.Line(win,start=(210,0), end=(-210,0), ori=-159),
           visual.Line(win,start=(228,0), end=(-228,0), ori=-35),
           visual.Line(win,start=(218,0), end=(-218,0), ori=-133),
           visual.Line(win,start=(203,0), end=(-203,0), ori=-131),
           visual.Line(win,start=(225,0), end=(-225,0), ori=-155),
           visual.Line(win,start=(203,0), end=(-203,0), ori=-164),
           visual.Line(win,start=(201.5,0), end=(-201.5,0), ori=-81),
           visual.Line(win,start=(224,0), end=(-224,0), ori=-30),
           visual.Line(win,start=(221.5,0), end=(-221.5,0), ori=-77),
           visual.Line(win,start=(197.5,0), end=(-197.5,0), ori=-114),
           visual.Line(win,start=(210,0), end=(-210,0), ori=-66),
           visual.Line(win,start=(222.5,0), end=(-222.5,0), ori=-165),
           visual.Line(win,start=(200,0), end=(-200,0), ori=-103),
           visual.Line(win,start=(198,0), end=(-198,0), ori=-113),
           visual.Line(win,start=(224.5,0), end=(-224.5,0), ori=-174),
           visual.Line(win,start=(199,0), end=(-199,0), ori=-78),
           visual.Line(win,start=(208.5,0), end=(-208.5,0), ori=-42),
           visual.Line(win,start=(206.5,0), end=(-206.5,0), ori=-39),
           visual.Line(win,start=(208.5,0), end=(-208.5,0), ori=-95),
           visual.Line(win,start=(225.5,0), end=(-225.5,0), ori=-168),
           visual.Line(win,start=(217,0), end=(-217,0), ori=-137),
           visual.Line(win,start=(212,0), end=(-212,0), ori=-123),
           visual.Line(win,start=(201,0), end=(-201,0), ori=-151),
           visual.Line(win,start=(225,0), end=(-225,0), ori=-129),
           visual.Line(win,start=(221,0), end=(-221,0), ori=-127),
           visual.Line(win,start=(202.5,0), end=(-202.5,0), ori=-78),
           visual.Line(win,start=(219,0), end=(-219,0), ori=-64),
           visual.Line(win,start=(218.5,0), end=(-218.5,0), ori=-140),
           visual.Line(win,start=(225.5,0), end=(-225.5,0), ori=-29),
           visual.Line(win,start=(223,0), end=(-223,0), ori=-161),
           visual.Line(win,start=(201,0), end=(-201,0), ori=-127),
           visual.Line(win,start=(219.5,0), end=(-219.5,0), ori=-156),
           visual.Line(win,start=(207.5,0), end=(-207.5,0), ori=-133),
           visual.Line(win,start=(218.5,0), end=(-218.5,0), ori=-51),
           visual.Line(win,start=(228.5,0), end=(-228.5,0), ori=-105),
           visual.Line(win,start=(226,0), end=(-226,0), ori=-139),
           visual.Line(win,start=(206,0), end=(-206,0), ori=-125),
           visual.Line(win,start=(212,0), end=(-212,0), ori=-93),
           visual.Line(win,start=(218.5,0), end=(-218.5,0), ori=-47),
           visual.Line(win,start=(206.5,0), end=(-206.5,0), ori=-86),
           visual.Line(win,start=(224,0), end=(-224,0), ori=-30),
           visual.Line(win,start=(224,0), end=(-224,0), ori=-64),
           visual.Line(win,start=(221.5,0), end=(-221.5,0), ori=-26),
           visual.Line(win,start=(225.5,0), end=(-225.5,0), ori=-115),
           visual.Line(win,start=(223,0), end=(-223,0), ori=-56),
           visual.Line(win,start=(223,0), end=(-223,0), ori=-149),
           visual.Line(win,start=(223.5,0), end=(-223.5,0), ori=-56),
           visual.Line(win,start=(215,0), end=(-215,0), ori=-99),
           visual.Line(win,start=(226,0), end=(-226,0), ori=-103),
           visual.Line(win,start=(204,0), end=(-204,0), ori=-85),
           visual.Line(win,start=(229,0), end=(-229,0), ori=-31),
           visual.Line(win,start=(222,0), end=(-222,0), ori=-123),
           visual.Line(win,start=(216.5,0), end=(-216.5,0), ori=-111),
           visual.Line(win,start=(223.5,0), end=(-223.5,0), ori=-58),
           visual.Line(win,start=(215,0), end=(-215,0), ori=-36),
           visual.Line(win,start=(202.5,0), end=(-202.5,0), ori=-52),
           visual.Line(win,start=(227,0), end=(-227,0), ori=-162),
           visual.Line(win,start=(208,0), end=(-208,0), ori=-27),
           visual.Line(win,start=(217.5,0), end=(-217.5,0), ori=-64),
           visual.Line(win,start=(199,0), end=(-199,0), ori=-27),
           visual.Line(win,start=(225.5,0), end=(-225.5,0), ori=-138),
           visual.Line(win,start=(210.5,0), end=(-210.5,0), ori=-93),
           visual.Line(win,start=(213.5,0), end=(-213.5,0), ori=-102),
           visual.Line(win,start=(225,0), end=(-225,0), ori=-160),
           visual.Line(win,start=(201.5,0), end=(-201.5,0), ori=-140),
           visual.Line(win,start=(204,0), end=(-204,0), ori=-82),
           visual.Line(win,start=(211,0), end=(-211,0), ori=-45),
           visual.Line(win,start=(203.5,0), end=(-203.5,0), ori=-171),
           visual.Line(win,start=(197.5,0), end=(-197.5,0), ori=-130),
           visual.Line(win,start=(205.5,0), end=(-205.5,0), ori=-101),
           visual.Line(win,start=(202,0), end=(-202,0), ori=-30),
           visual.Line(win,start=(225.5,0), end=(-225.5,0), ori=-66),
           visual.Line(win,start=(217.5,0), end=(-217.5,0), ori=-34),
           visual.Line(win,start=(221.5,0), end=(-221.5,0), ori=-62),
           visual.Line(win,start=(212,0), end=(-212,0), ori=-139),
           visual.Line(win,start=(219.5,0), end=(-219.5,0), ori=-71),
           visual.Line(win,start=(212,0), end=(-212,0), ori=-139),
           visual.Line(win,start=(199,0), end=(-199,0), ori=-136),
           visual.Line(win,start=(230,0), end=(-230,0), ori=-158),
           visual.Line(win,start=(213.5,0), end=(-213.5,0), ori=-172),
           visual.Line(win,start=(208.5,0), end=(-208.5,0), ori=-116),
           visual.Line(win,start=(219.5,0), end=(-219.5,0), ori=-94),
           visual.Line(win,start=(210,0), end=(-210,0), ori=-114),
           visual.Line(win,start=(221.5,0), end=(-221.5,0), ori=-53),
           visual.Line(win,start=(214,0), end=(-214,0), ori=-161),
           visual.Line(win,start=(210,0), end=(-210,0), ori=-57),
           visual.Line(win,start=(199.5,0), end=(-199.5,0), ori=-112),
           visual.Line(win,start=(206.5,0), end=(-206.5,0), ori=-62),
           visual.Line(win,start=(217,0), end=(-217,0), ori=-38),
           visual.Line(win,start=(197.5,0), end=(-197.5,0), ori=-161),
           visual.Line(win,start=(218.5,0), end=(-218.5,0), ori=-44),
           visual.Line(win,start=(219,0), end=(-219,0), ori=-161),
           visual.Line(win,start=(224,0), end=(-224,0), ori=-173),
           visual.Line(win,start=(222.5,0), end=(-222.5,0), ori=-40),
           visual.Line(win,start=(205,0), end=(-205,0), ori=-55),
           visual.Line(win,start=(214,0), end=(-214,0), ori=-146),
           visual.Line(win,start=(216.5,0), end=(-216.5,0), ori=-44),
           visual.Line(win,start=(210,0), end=(-210,0), ori=-91),
           visual.Line(win,start=(227,0), end=(-227,0), ori=-43),
           visual.Line(win,start=(229,0), end=(-229,0), ori=-160)]
    
    #categories RB
    def cat(index):
        if index < 300: #should be 300
            return ['d']
        else:
            return ['k']
    
    
    index=range(len(lines))
    trials=data.TrialHandler(index, 1)
    
    experiment.addLoop(trials)
    count = 0
    
    for trial in trials:
        
        if event.getKeys(keyList='1'):
            x = error
        
        #new block text
        num_block = (trials.thisTrialN / 50) + 1
        experiment.addData('Block Number', num_block) #add block number to sheet
        new_block_text=visual.TextStim(win, text='Now beginning Round '+str(num_block), color=[1,1,1], height = 50)
    
        #button switch text
        button_switch='Respond quickly and the response buttons will now be switched.'
        button_switch_text=visual.TextStim(win, text=button_switch, color=[1,1,1], height = 40, wrapWidth=1000)
        
        fast = False
        
        if (trials.thisTrialN) % 50 == 0:
            #draw now starting block number
            new_block_text.draw()
            win.flip()
            core.wait(2)
            
            count = 0 #how many correct
            if trials.thisTrialN == 500:
                #draw new instructions for button switching
                button_switch_text.draw()
                win.flip()
                core.wait(3)
                fast = True
                experiment.addData('Button switch shown?', 'Y')
                
        if trials.thisTrialN >= 500: #Round 11 and after
            fast=True
            experiment.addData('Actually switched?', 'Y')

        lines[trial].draw()
        win.flip()
        if fast == True:
            input = event.waitKeys(1.5, keyList=['d', 'k'])
            experiment.addData('Key pressed', input)
            experiment.addData('Fast?', 'Y')
        else:
            input = event.waitKeys(5, keyList=['d', 'k'])
            experiment.addData('Key pressed', input)
        if input==None: #if no response
            experiment.addData('Correct?', 'Timed out') #edit
            if fast == True:
                go_go=visual.TextStim(win, text='Please respond within 1.5 seconds.', color=[1,1,1], height = 40)
                go_go.draw()
                win.flip()
                core.wait(1)
            else:
                go=visual.TextStim(win, text='Please respond within 5 seconds.', color=[1,1,1], height=40)
                go.draw()
                win.flip()
                core.wait(1)
            #trial discarded
        else: #if there is a response
            correct_cat=cat(trials.thisIndex)
            experiment.addData('Category', correct_cat)
            if input == correct_cat:
                if fast == True: #button switched
                    experiment.addData('Correct?', 'N')
                    wrong=visual.TextStim(win, text='Wrong', color=[1,1,1], height=50)
                    w_sound=sound.SoundPyo(value=200, secs=1)
                    wrong.draw()
                    w_sound.play()
                    win.flip()
                    core.wait(1)
                else:
                    #save the data that this was right
                    experiment.addData('Correct?', 'Y')
                    count += 1
                    #show correct!
                    correct=visual.TextStim(win, text='Correct', color=[1,1,1], height=50)
                    r_sound=sound.backend_pyo.SoundPyo(value=500, secs=1)
                    correct.draw()
                    #make a sound!
                    r_sound.play()
                    win.flip()
                    core.wait(1)
            else:
                if fast == True:
                    experiment.addData('Correct?', 'Y')
                    count += 1
                    #show correct!
                    correct=visual.TextStim(win, text='Correct', color=[1,1,1], height=50)
                    r_sound=sound.SoundPyo(value=500, secs=1)
                    correct.draw()
                    r_sound.play()
                    win.flip()
                    core.wait(1)
                else:
                    #show wrong
                    experiment.addData('Correct?', 'N')
                    wrong=visual.TextStim(win, text='Wrong', color=[1,1,1], height=50)
                    w_sound=sound.backend_pyo.SoundPyo(value=200, secs=1)
                    wrong.draw()
                    w_sound.play()
                    win.flip()
                    core.wait(1)
        core.wait(1)
        
        
        if (trials.thisTrialN + 1) % 50 == 0: #if the next trial is beginning of new block
            #show block accuracy
            acc_count_percent=str(count*2)+'% Accurate'
            current_round_num=visual.TextStim(win, text='Block '+str((trials.thisTrialN+1)/50), color=[1,1,1], pos=(0,100), height=50)
            accu_rate_text=visual.TextStim(win, text=acc_count_percent, color=[1,1,1], height=50)
            current_round_num.draw()
            accu_rate_text.draw()
            win.flip()
            experiment.addData('Total correct', count)
            experiment.addData('Percent correct', acc_count_percent)
            core.wait(3)
        
        experiment.nextEntry()
        
        
    end_text=visual.TextStim(win,text='The experiment has concluded. Please gather your belonging and exit the testing room. If you have any questions, feel free to ask the experimenter. Thank you for your participation!', color=[1,1,1], height=40)
    end_text.draw()
    win.flip()
    core.wait(10)
    
else:
    print ('Experiment information collection unsuccessful!')
