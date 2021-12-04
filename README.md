# deergroup

PETE 219: Data Analytics Group Project
Instructors: Thomas Seers, Harris Rabbani & Abdul Karim Mohamed

thomas.seers@qatar.tamu.edu
harris.rabbani@qatar.tamu.edu

Introduction	
In groups of three, you will utilize the concepts and methods that you have acquired during PETE 219 to undertake a data analytics project using key subsurface datasets:
1.	Well logs
2.	Poro-perm / facies description datasets
3.	Pore-scale micro CT images of reservoir rocks

This project will contribute 15% towards your total mark for PETE 219. Specifically, you will utilize these datasets to assess the reservoir quality and reservoir potential for a single exploration well. Though appreciated, technical insights from the subsurface perspective are less critical in this assessment than the technical ability in data analytics demonstrated in your Python project’s workflow. Another key thing to consider is that any attempt to move beyond the tools and concepts presented within PETE 219 will be greatly appreciated and rewarded: you cannot learn to code without exploring Python’s vast functionality yourselves!

Tasks
Project Management
You are required to manage your project using GitHub. You will need to select one group member as the project owner, with the other group members acting as collaborators. You GitHub project should contain your data, code and ancillary items (README.md, report, presentation: more on that shortly). We will actively look for evidence of collaboration on your GitHub project (edits / commits). 
 
Well Log Analysis
For your wireline log data, you need to approach the analysis in a stepwise fashion:
1.	Data import and cleaning: what libraries did you use to parse your data? What exploratory data analysis did you perform to identify anomalies/outliers? What artifacts did you encounter in your raw dataset and what was your strategy for cleaning these anomalous elements (replacement with null values / nan, interpolating between nearest neighbors, flipping sign etc.)? 

2.	Data visualization. you should aim to display your log data in multiple ways: e.g. classic log profiles, histograms of log properties, cross-plots of potentially correlated properties etc. Credit will be given for going beyond the lab examples provided within PETE 219 (for example can you plot the neutron-density plot with infill / put your logs on a single plot? See below and https://towardsdatascience.com/enhancing-visualization-of-well-logs-with-plot-fills-72d9dcd10c1b) 

3.	Data analysis: consider which logging suites are most valuable for assessing reservoir quality and potential and focus on these: GR, RILD-RIL3, CNPOR-RHOB). The basic target of your analysis should be the following: v-shale cutoff and net-to-gross; locating high quality reservoir facies (GR) and correlating these with potential oil/gas shows (estimating total reservoir thickness / hydrocarbon column height, differentiating oi vs. gas reservoir etc.; assessing the distributional form of various log properties (negative vs. posite skew etc.); locating correlateable properties (linear regression). Credit wioll be given for the development of bespoke functions applied to your data frame (e.g. calculating effective stress from RHOB and DEPTH)


Deliverables:

1.	A GitHub project containing all code, data and ancillary materials associated with the group project (readme.mp, report, 
2.	Group report: maximum 3000-word group report detailing your analysis workflow. Appendices should be provided containing your code scripts and referenced within the text.
3.	A 20-minute presentation summarizing your findings, to be delivered in the final lab of PETE 219. Myself, Dr Harris and Abdul

