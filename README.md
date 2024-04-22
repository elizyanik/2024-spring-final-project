# Data Visualization Spring 2024 Final Project

## Introduction

The final project for the semester will simulate use of data management and visualization techniques we have covered so far in a professional setting. The goal of the project is to choose a dataset, extract original insights from it which pertain to a meaningful problem, visualize the results, and produce a professional report in a Jupyter notebook. You are required to select a dataset which pertains to a *problem* of interest to you. A problem is an unsolved issue which causes a pain in a being, organization, or society.

You are not required to solve the unsolved problem that you select, but you are required to extract insights from the problem which are completely original. When deciding what insights you want to extract, ask yourself, would someone want to work with me on this problem in a professional setting if they saw the insights I extracted, or would they assume that anyone else (or any AI tool) could have easily extracted the same insights?

No starter code will be provided. The goal of the project is to independently produce an in-depth analysis which extracts and professionally reports on insights gained from a data set about a problem of significance to a field you are interested in. Here we specify the project deliverables, requirements, grading criteria, and policies on collaboration with humans and AI tools.

While you may not choose a problem that you are working on directly in another class, choosing a problem which pertains to your general field, research, academic, or professional interests is highly encouraged. If you are not sure what problem to pick, problem choices can be discussed in office hours.

## Deliverables

Three project deliverables shall be provided.

* **Project Abstract**: Write one paragraph in a README file specifying what problem you are going to be analyzing, where you can get data about that problem, what techniques you think you might be able to apply to it, and what insights you plan to attempt to extract from it. The project abstract is due the same day as the project itself, but it is highly recommended to review your topic idea with your instructor first. Sending via email or discussing in office hours are both acceptable.
* **Project Notebook**: This is the main artifact of the final project. It should be a professionally written report on your problem and the insights you gained from it, including any data management techniques you used to extract those insights and visualizations which display them.
* **Project Modules**: Rather than developing large chunks of code in your Jupyter notebook, you are required to implement complex functions in their own modules and call these modules from your notebook. There should be a minimal amount of code in your Jupyter notebook.

All deliverables shall be provided by **11:59 PM** at the end of the exam period, **05/08**. Please submit via git but note that no points will be deducted for an improper git submission for this project. Git submission mechanics were assessed in the beginning of the semester. The goal of this assignment is to assess your ability to extract original insights to tell a data driven story that is entirely your own.

## Requirements

The following project requirements on format, technical depth, insight, software, technical communication, and use of techniques from class shall be adhered to.

### Format

The project Notebook deliverable shall be written as a professional report in the following format. Each bullet should be a top level section in your notebook.

* **Introduction**: Write 1-2 paragraphs introducing the problem and dataset you are studying. Review the rest of the sections of the notebook. Explain what techniques you will be applying and why you are applying them. Employ a visual to show the problem or dataset you are studying at a glace.
* **Motivation**: Write a paragraph explaining why you are studying this problem and why the reader should care about the insights you gain from it. There are many problems to be solved in the world. Explain why yours matters!
* **Contribution**: Explain what the most novel aspects of your methods are. Write a paragraph describing your contribution to this problem. Ensure that you are making a contribution that has not been made before! (Why should we read your report if you are just making a contribution that has already been made?)
* **Methods**: Explain the methods you are using to study your problem or dataset. Include a subsection for each method you employed. Explain why you chose each method. Write at least a short paragraph for each method used.
* **Main Results**: Present the main results here. Be sure to employ at least three techniques from class (see the grading rubric). Include a subsection for each main result that include the visualizations of the result and a short paragraph explaining each.
* **Conclusion**: Summarize your findings and contributions in a paragraph here.

### Guidance on Novelty and Insight

There are novel problems and old problems. There are also novel methods of attacking problems and old methods of attacking them. This means there are four types of contributions. Three of them are novel.

1. We can attack an old problem with an old method. This does not constitute a novel contribution, but can be valuable if we explain the solution in a way that is better than others who have applied these methods have done before.
2. We can attack an old problem with a new method. This is a novel contribution. We can show why our contribution matters by explaining why we think our new methods will bring new insights into the old problem that many others have studied before.
3. We can attack a new problem with an old method. This is also a novel contribution. Sometimes an old method can solve new problems that have emerged since the method was originally developed. These discoveries are quite exciting since they show us how existing tools can solve emergent problems.
4. We can also attack new problems with new methods. This is where cutting edge research is performed. There is a wealth of novelty to be found in this region of the problem-solution space!

Project notebooks shall make at least one novel insight. Any type 2, 3, or 4 insight is a novel one.

In a professional setting, a novel contribution can be pragmatically thought of as one which someone would hire you on the job to perform. In an informal setting, a novel contribution is one that someone else equally knowledgeable about your field would be interested in discussing with you (and perhaps might even find interesting enough to pay for your meal or drink)!

### Technical Depth

Deliverables shall be of graduate level technical depth. Indicators of graduate level technical depth include the following.

* Multiple sources shall be surveyed and cited. If others have worked on your problem before, be sure to cite a few examples.
* The source of the data used shall be cited.
* The data shall be analyzed with multiple methods. Benefits, challenges, tradeoffs, and limitations of each method shall be discussed. For example, if you use correlation analysis, be sure to discuss the limitations of what can be concluded therefrom.
* The analyses performed shall show consideration to practical issues, such as noise in the data, considerations for the limitations of correlation, considerations for visualizing high dimensionality, etc.
* You do not need to solve your unsolved problem (the assignment deadline is far too short for that!) but all notebooks shall present novel ways of thinking about the problems selected.

### Software

The software used shall follow the principals of software hygiene discussed in class. All lengthy functions (> 20 lines) shall be written in reusable modules and imported into the notebook deliverable. The software written shall run outside your local environment (e.g., in codespaces) with no trouble. This means functions for loading the data or downloading it off the internet must be written in a reusable manner which does not reference local paths.

### Technical Communication

Project notebooks shall showcase professional technical communication skills. Project notebooks shall be divided into well structured sections and shall use markdown to specify headings for each section. Project notebooks shall use LaTeX within markdown to typeset equations (AI tools are great for helping with this). Project notebooks shall be written in full sentences and well-constructed paragraphs (3-10 sentences per paragraph). Writing shall guide readers through the material by narrating where they are in the document and explaining where they are going next.

### Use of Techniques from Class

Project notebooks shall include at least one interactive visualizations. You may use any of the methods learned in class to produce these.

Project notebooks shall additionally use at least three techniques that we have learned from class so far. Candidate techniques include:

* DataFrame masking, combination, and other operations. Use of any of these counts as a single technique, e.g., if you apply masking and DataFrame combination, that counts as one technique.
* Use of NumPy to accelerate performing computations on our data.
* Use of MatPlotLib to generate tightly controlled figures.
* Use of LaTeX to typeset mathematical symbols in plots.
* Representation of multivariate data using colors, markers, 3D plots, and interactive plots.
* Use of convolution to find patterns in data.
* Use of mathematical transforms to extract insights from data (Fourier, Short Time Fourier, Hilbert, or other).
* Use of polynomial fitting to find trends in data.
* Use of principal component analysis to reduce high dimensional data to a low dimensional space for visualization.
* Use of nonlinear transforms (logarithmic scaling, conversion to decibels, removing data below a threshold) to enhance our visualizations.
* Use of histograms to represent distributions and use of combined scatter and histograms to represent joint and marginal distributions.
* Use of correlation and mutual information to test if two variables are related.
* Use of interactive plots (using any tools we have covered) to explore data.
* Use of holoviews to abstract our plotting code away from the underlying plotting backend.
* Use of geopy to obtain geographic data.
* Use of geopandas and geoviews to plot shapes and lines on a map.
* Use of pymap3d to handle coordinate conversions when working with geographic data.
* Use of color to represent mathematical objects in the complex domain.
* Use of state spaces to visualize how an object's kinematic state changes with time.
* Visualization of machine learning results.
* Explaining machine learning results with attributions techniques.
* Use of generative AI to create visualizations.
* Visualization of machine learning models themselves.
* Using clustering to visualize groups of data.
* Use of machine learning models to classify regions of data.
* Application of visual question answering to create natural language interfaces to our plots.

## Grading Rubric

The project will be graded out of 100 points.

### Originality (25%)

The following criteria will be used to assess the originality of a project.

#### Choice of Problem and Dataset

Project notebooks shall represent an analysis of a problem of interest to the student's field of choice and explain why it is of interest to this community. Notebooks lacking explanation of why a problem is of interest will lose **5 points**.

#### Original Steps to Visualize the Problem

Project notebooks shall go beyond simply calling available functions from one or two popular libraries and shall instead take original steps to analyze the problem by combining tools from many libraries in unique ways. Notebooks which use < 2 tools to perform a straightforward analysis (e.g., simply generate some default plots) will lose **5 points**.

#### Original Insights Gained from the Visualizations

Project notebooks shall extract at least one novel insight from the dataset chosen. Projects which do not extract a novel insight will lose **5 points**.

See the section providing [guidance on novelty](#guidance-on-novelty-and-insight).

#### Actionability of the Insights

The insights presented by project notebooks shall be actionable. For each insight presented, ask yourself, can the reader take action from it? What action would they take? If these questions are difficult to answer, then the information presented is not actionable. Three actionable insights shall be presented per project. A notebook without enough actionable insights will lose **5 points**.

#### Original Exposition of the Insights

The insights shall be exposited in an original manner. Each insight should be explained in an original manner, in your own words. Use analogies and other explanatory devices to help the reader see the insights you have extracted from the data and take action on them.

#### Original Code and Work

All code and writing must be the student's own work. See the policies on [collaboration](#policy-on-collaboration), [use of AI](#policy-on-use-of-ai), and the course policy on academic integrity. Any violations of these policies will result in a zero grade.

### Software Hygiene (25%)

#### Use of Modules

Any functions longer than 20 lines of code shall be implemented in importable modules. If any functions greater than 20 lines of code implemented within project notebooks, **5 points** will be deducted.

#### Ensure Your Code Runs in Any Environment

Project notebooks shall be executable in any of the environments studied in class (local machine or codespaces). Project notebooks shall not contain local paths specific to your machine. Project notebooks shall include code to download your data or, if this is not possible, shall include data in version control with the project (note that this is not a best practice, but is acceptable for this assignment). Projects which include code that will not be executable outside your local environment will lose **5 points**

#### High Quality Documentation

All project deliverables shall provide high quality documentation. All functions shall have docstrings. Use comments, but do not comment every line of code. Write code that is self-explanatory and does not need a comment for every line. Ensure the notebook reads like a professional report. Notebooks and modules without high quality documentation will lose **5 points**.

#### Use of a Style Guide

Project notebooks shall be styled with `black`. You do not need to use automatic formatting (though you are encouraged to). Running `black` once before submission is sufficient. Projects clearly unstyled will lose **2.5 points**.

#### Quality of Commit Messages

Write high quality commit messages using the guidance learned in class. A good commit message should read `"When applied, this commit will...[insert your message here]"`. Poor quality commit messages will lose **2.5 points**.

#### Descriptive Variable and Function Names

Variable names shall be descriptive nouns. Function names shall be descriptive verbs. One letter variable names shall not be used. Variables which store measured quantities shall include the units of the measured quantities in their names. Poor quality variable names will lose **2.5 points**.

#### Dead Code

Project notebooks shall contain no commented out or dead code. Notebooks with dead code with lose **2.5 points**.

### Data Management and Visualization Professionalism (35%)

#### Technical Communication

The following deductions will be applied for technical communication considerations.

* Notebooks shall adhere to the [project format](#format). Notebooks that do not will lose **5 points**.
* Notebook shall use full sentences and paragraphs. Writing that is not in full sentences and paragraphs will lose **5 points**.
* Notebooks shall use a spell checker. Numerous spelling errors (> 5) will lose **2 points**.
* Notebooks shall be written in clear expository tone. Do not use an exploratory tone, e.g., do not write "here we try X, it didn't work, so instead let's try Y". Exploratory tone is encouraged in exploratory notes, but this project will produce a final deliverable! Exploratory tone will result in a **2 point** deduction.
* Do not forget to make the goal of each notebook section clear to the reader. Failure to narrate where the reader is in the notebook will result in a **1 point** deduction.

#### Visualization - Minor Point Deductions

Violation of any of the following requirements will result in a loss of 2 points each, up to **20 points lost maximum**.

* Plots shall not waste ink per Tufte's definition.
* Plots shall not tell lies per Tufte's definition.
* Plots shall be in the correct domain (e.g., time, frequency, etc.) for the data being used. The domain which maximizes the apparent signal to noise ratio in the plot is the correct domain.
* Plot labels shall not run into the axes.
* Plot labels shall not run into other labels.
* Bivariate data shall use the correct axes.
* Data shall employ the correct choice of plot type.
* Multidimensional plotting techniques that do not waste ink (markers, color) shall be employed for multidimensional data.
* Interactive plots shall be employed for data with too many dimensions to visualize.
* Multiple axes shall be employed if plotting data with different scales in the same plot.
* Dimensionality reduction shall be applied to visualize high dimensional data, but only when this preserves the structure of the data (e.g., classes are still separable in a machine learning problem).
* Plots of statistical data shall include uncertainty and error bounds where applicable.
* Plots shall show both joint and marginal distributions when available.
* Polynomial fitting with an appropriate number of coefficients shall be applied to smooth noisy data.
* The correct coordinate frame shall be used to display map data.

#### Visualization - Major Point Deductions

Violation of any of the following requirements will result in a loss of **5 points** each, up to a **maximum of 20 points** lost.

* Any correlations used shall be inspected for validity.
* Correlation shall not be used to imply causation.
* The lack of correlation shall not be used to imply the lack of a relationship.
* Correlation shall not be applied across clusters.
* Outliers shall be removed before applying correlation.
* Mutual information shall be employed to test data that is not correlated for a nonlinear relationship.
* The correct mutual information estimation technique (continuous or discrete) shall be employed.

### Basics (15%)

#### Proper Use of Functions and Lambdas

Functions and lambdas shall be implemented correctly without logical or execution errors (3 points).

#### Proper Use of Conditional Statements, For Loops

Conditional statements and for loops shall be implemented correctly without logical or execution errors (3 points).

#### Proper Use of Data Structures

The correct Python data structures shall be used (Lists, Dictionaries, Tuples, etc.) for the correct applications (3 points).

#### Proper Use of NumPy

NumPy shall be used for code that operates with arrays. Array operations shall be used instead of for loops (3 points).

#### Proper Use of DataFrames

DataFrames shall be used properly (3 points).

* The `apply()` function shall be used to iterate a function over a DataFrame.
* Use `to_list` and `to_numpy` functions shall be used to extract lists and arrays from a DataFrame.
* Rows, columns, and elements shall be accessed properly.
* Masks shall be used correctly to select data.

## Policy on Collaboration

Students are allowed to collaborate on the final project (e.g., to debug an error), however, all work in the deliverables must be your own and the following rules shall be adhered to.

* Do not use the same code as another student.
* Do not extract the same insights as another student.
* Do not collaborate with others outside the class (e.g., a student who took the course previously).
* Do not submit work that is not your own.

Any violations of these policies will result in a grade of **zero** for the final project. In a professional setting, it is important to extract insights from data that our competition cannot. Why hire a new developer or a new firm if they produce the same insights a current contract is producing? Originality is critical to maintaining a competitive edge and will be graded accordingly.

## Policy on use of AI

Using AI tools to help you write code is allowed, however, do not do violate any of the following rules.

* Do not provide code written by AI tools without adding any original work to it. If you just learn to use AI to perform tasks, why hire you when the AI can do the work cheaper and without getting tired?
* Do not provide code written by AI without checking that it actually does what you think it does.
* Do not use AI in a way that violates the Veterinary Dentists law, i.e., ensure you have knowledge of the AI tools you are using AND knowledge of the domain in which you are applying them. For example, do not use AI to perform analysis of a dataset in a field you know nothing about without researching that field extensively to ensure the AI results are correct, and do not use AI to perform an analysis in a field you are an expert about unless you provide citations to the AI tools you are using and can demonstrate you understand how they work, and how they arrived at the insights you acquired from them.

Any violations of these policies will result in a grade of **zero** for the final project. In a professional setting, it is important to extract insights from data that AI cannot alone. Why hire a new developer or a new firm if they produce the same insights that the hiring body can produce with AI? AI can perform many tasks cheaper and faster than humans. Use this assignment to practice using AI as a tool to expand your own original insights rather than as a tool to replace yourself!

## Anti-Patterns to Avoid

The following anti-patterns shall be avoided. Ask if you have a question about any of these. Unless specified elsewhere, each occurrence of these anti-patterns will result in a **2.5 point deduction** so please be careful!

### Visualization Anti-Patterns

* Do not show plots with no title.
* Do not show plots with no axis labels.
* Do not show plots where axis ticks and associated text run together.
* Do not show plots where the axes labels or titles are too small to see.
* Do not show plots with more labels or more x-ticks than anyone can reasonably see.
* Do not show plots which show multiple relationships with no legend.
* Do not show subplots that run into other plots.
* Do not show dates in non-date format (e.g., year 2000.5).
* Do not use grid lines unnecessarily.
* Do not show noisy data without extracting a smooth trend or determining that no trend exists!
* Do not show axes in unnatural units (please scale data so that there are only 3 numbers before the decimal place, e.g., 50 km rather than 5e4 m).
* Do not showing statistical data without showing uncertainty.
* Do not use one-dimensional scatter plots to convey a distribution over a single independent variable, rather than using histograms, violin plots or other appropriate means of showing statistical data.
* Do not plot too many subplots without expanding the width or height of the figure to accommodate them.
* Do not show a correlation matrix without investigating the correlations for realism and investigating variables that are not correlated for mutual information with other variables (e.g., do not simply use `sns.PairGrid` or `sns.heatmap` without doing any other work)!

### Typesetting Anti-Patterns
* Do not write mathematical symbols in informal notation, e.g., `e^(sin(x))` rather than $e^{\sin(x)}$.
* Do not include cells that produce errors in your finished notebook.
* Do not leave necessary warnings unsuppressed in your notebook.
* Do not leave unnatural notation from the code in the plot labels (e.g., do not show a Y axis labelled `my_dataframe_col_with_altitude` instead of taking the time to label the axis `Altitude (km)`).
* Do not reference a quantity without specifying its units unless working with purely mathematical objects.
* Use proper capitalization in plot labels and axes.

### Technical Communication Anti-Patterns
* Do not turn in notebooks with spelling mistakes (please use a spell checker).
* Do not turn in notebooks with incomplete sentences.
* Do not use an exploratory tone, e.g., do not write "here we try X, it didn't work, so instead let's try Y". Exploratory tone is encouraged in exploratory notes, but this project will produce a final deliverable!
* Do not forget to make the goal of each notebook section clear to the reader.

### Software Anti-Patterns
* Do not develop large blocks of code inside a notebook. Instead, make them available as reusable modules.
* Do not use paths specific to your local machine or personal development environment.
* Do not use for loops where NumPy can be used instead.
* Do not write overly lengthy lines (> 120 characters, or > 80 if you use `black`).
* Do not comment every line.
* Do not use single letter variable names.
* Do not leave commented out code in your notebook.

### Anti-Patterns Showing Lack of Originality
* Do not use the same exact code as another student (this **will result in a zero** - see collaboration policy and policy on academic integrity).
* Do not use code directly from an AI tool without performing any original work on the code (this **will result in a zero** - see AI policy and policy on academic integrity).
* Do not use plots using common tools without performing any transformations on data or explaining what insights the plots reveal (e.g., simply generating a correlation matrix without performing any investigation around which correlations are valid and what they mean).
