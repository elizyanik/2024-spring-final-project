# Data Visualization Spring 2024 Final Project

## Introduction

The final project for the semester will simulate use of data management and visualization techniques we have covered so far in a professional setting. The goal of the project is to choose a dataset, extract original insights from it which pertain to a meaningful problem, visualize the results, and produce a professional report in a Jupyter notebook. You are required to select a dataset which pertains to a *problem* of interest to you. A problem is an unsolved issue which causes a pain in a person, society, or organization.

You are not required to solve the unsolved problem that you select, but you are required to extract insights from the problem which are completely original. When deciding what insights you want to extract, ask yourself, would someone what to work with me on this problem in a professional setting if they saw the insights I extracted, or would they assume that anyone (or any AI tool) could have easily extracted the same insights?

No starter code will be provided. The goal of the project is to, by working only from minimally specified requirements, independently produce an in-depth analysis which extracts and professionally reports on insights gained from a data set about a problem of significance to a field you are interested in. Here we specify the project deliverables, requirements, grading criteria, and policies on collaboration with humans and AI tools.

While you may not choose a problem that you are working on directly in another class, choosing a problem which pertains to your general field, research, academic, or professional interests is highly encouraged.

## Deliverables

Three project deliverables are required:

* **Project Abstract**: Write one paragraph in a README file specifying what problem you are going to be analyzing, where you can get data about that problem, what techniques you think you might be able to apply to it, and what insights you plan to attempt to extract from it. The project abstract is due the same day as the project itself, but it is highly recommended to review your topic idea with your instructor first. Sending via email or discussing in office hours are both acceptable.
* **Project Notebook**: This is the main artifact of the final project. It should be a professionally written report on your problem and the insights you gained from it.
* **Project Modules**: Rather than developing large chunks of code in your Jupyter notebook, you are required to implement complex functions in their own modules and call these modules from your notebook. There should be a minimal amount of code in your Jupyter notebook.

All deliverables are due **11:59 PM** at the end of the exam period, **05/08**. Please submit via git but note that no points will be deducted for an improper git submission for this project. Git submission mechanics were assessed in the beginning of the semester.

## Requirements

The following project requirements on format, technical depth, insight, software, technical communication, and use of techniques from class shall be adhered to.

### Format

The project Notebook deliverable shall be written as a professional report in the following format. Each bullet should be a top level section in your notebook.

* **Introduction**: Write 1-2 paragraphs introducing the problem and dataset you are studying. Review the rest of the sections of the notebook. Explain what techniques you will be applying and why you are applying them. Employ a visual to show the problem or dataset you are studying at a glace.
* **Motivation**: Write a paragraph explaining why you are studying this problem and why the reader should care about the insights you gain from it. There are many problems to be solved in the world. Explain why yours matters!
* **Contribution**: Explain what the most novel aspects of your methods are. Write a paragraph describing your contribution to this problem. Ensure that you are making a contribution that has not been made before! (Why should we read your report if you are just making a contribution that has already been made?)
* **Methods**: Explain the methods you are using to study your problem or dataset. Include a subsection for each method you employed. Explain why you chose each method. Write at least a short paragraph for each method used.
* **Main Results**: Present the main results here. Be sure to employ at least four techniques from class (see the grading rubric). Include a subsection for each main result that include the visualizations of the result and a short paragraph explaining each.
* **Conclusion**: Summarize your findings and contributions in a paragraph here.

### Guidance on Novelty

There are novel problems and old problems, and novel methods of attacking them and old methods of attacking them. This means there are four types of contributions. Three of them are novel.

1. We can attack an old problem with an old method. This does not constitute a novel contribution, but can be valuable if we explain the solution in a way that is better than others who have applied these methods have done before.
2. We can attack an old problem with a new method. This is a novel contribution. We can show why our contribution matters by explaining why we think our new methods will bring new insights into the old problem that many others have studied before.
3. We can attack a new problem with an old method. This is also a novel contribution. Sometimes old method can solve new problems that have emerged since the method was originally developed. These discoveries are quite exciting since they show us how existing tools can solve emergent problems!
4. We can also attack new problems with new methods. This is where cutting edge research is performed. There is a wealth of novelty to be found in this region of the problem-solution space!

Any type 2, 3, or 4 insight is a novel one.

### Technical Depth

### Insight

### Software

### Technical Communication

Project notebooks shall showcase professional technical communication skills. Project notebooks shall be divided into well structured sections and shall use markdown to specify headings for each section. Project notebooks shall use LaTeX within markdown to typeset equations (AI tools are great for helping with this). Project notebooks shall be written in full sentences and well-constructed paragraphs (3-10 sentences per paragraph). Writing shall guide readers through the material by narrating where they are in the document and explaining where they are going next.

### Use of Techniques from Class

You are required to include at least two interactive visualizations. You may use any of the methods learned in class to produce these.

You must additionally use at least four techniques that we have learned from class so far. Candidate techniques include:

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

### Originality (25%)

#### Original Choice of Problem and Dataset

#### Value of the Problem

#### Original Steps to Visualize the Problem

#### Original Insights Gained from the Visualizations

#### Actionability of the Insights

#### Original Code and Work

#### Original Exposition of the Insights

### Software Hygiene (25%)

#### Initialization of Variables

#### Use of Modules

#### Ensure Your Code Runs in Any Environment

* No local paths
* Include code to download your data or commit your data with your project

#### Use of a Style Guide

#### Quality of Commit Messages

#### Descriptive Variable and Function Names

#### Dead Code

#### High Quality Documentation

* All functions must have docstrings
* Do not comment every line of code
* The notebook should read like a professional report

### Data Management and Visualization Professionalism (25%)

#### Notebook is Well Structured

#### Writing is in Full Sentences and Paragraphs

#### Plots with Wasted Ink

#### Plots that tell Lies

#### Plots in the Wrong Domain

#### Plots with Labels that Run into Axes

#### Plots with Labels that Run into Other Labels

#### Proper Plotting of Bivariate Data

* Correct axes
* Correct choice of plot type

#### Proper Plotting of Multivariate Data

* Use of multidimensional plotting techniques that do not waste ink (markers, color)
* Use of interactive plots for data with too many dimensions to visualize
* Use of multiple axes to plot data with different scales in the same plot
* Use of 3D plots

#### Proper Use of Dimensionality Reduction Techniques

#### Proper Representation of Uncertainty

#### Showing Joint and Marginal Distributions where Available

#### Showing N-sigma Bounds

#### Showing Error Bounds where Applicable

#### Proper Use of Correlation and Mutual Information

* Correlations inspected for validity
* Does not use correlation to imply causation
* Does not consider absence of correlation to indicate lack of a relationship
* Does not correlate across clusters
* Removes outliers before applying correlation
* Uses correct mutual information estimation techniques

#### Proper Application of Polynomial Fitting

#### Correct Coordinate Frame Usage

#### Display of Geographic Data on a Map

### Basics (25%)

#### Proper Use of Functions and Lambdas

#### Proper Use of Conditional Statements, For Loops

#### Proper Use of Data Structures

#### Proper Use of NumPy

#### Proper Use of DataFrames

* Use `apply()` to iterate a function over a DataFrame
* Use `to_list` and `to_numpy`
* Proper access to rows, columns, and elements
* Proper use of masks to select data

## Policy on Collaboration

Students are allowed to collaborate on the final project (e.g., to debug an error), however, all work in the deliverables must be your own and the following rules shall be adhered to.

* Do not use the same code as another student.
* Do not extract the same insights as another student.
* Do not collaborate with others outside the class (e.g., a student who took the course previously).
* Do not submit work that is not your own.

Any violations of these policies will result in a grade of **zero** for the final project. In a professional setting, it is important to extract insights from data that our competition cannot. Why hire a new developer or a new firm if they produce the same insights a current contract is producing? Originality is critical to maintaining a competitive edge and will be graded accordingly.

## Policy on use of AI

Using AI tools to help you write code is allowed, however, do not do violate any of the following rules.

* Do not provide code written by AI without adding any original work to it. If you just learn to use AI to perform tasks, why hire you when the AI can do the work cheaper and without getting tired?
* Do not provide code written by AI without checking that it actually does what you think it does.
* Do not use AI in a way that violates the Veterinary Dentists law, i.e., ensure you have knowledge of the AI tools you are using AND knowledge of the domain in which you are applying them. For example, do not use AI to perform analysis of a dataset in a field you know nothing about without researching that field extensively to ensure the AI results are correct, and do not use AI to perform an analysis in a field you are an expert about unless you provide citations to the AI tools you are using and can demonstrate you understand how they work, and how they arrived at the insights you acquired from them.

Any violations of these policies will result in a grade of **zero** for the final project. In a professional setting, it is important to extract insights from data that AI cannot alone. Why hire a new developer or a new firm if they produce the same insights that the hiring body can produce with AI? AI can perform many tasks cheaper and faster than humans. Use this assignment to practice using AI as a tool to expand your own original insights rather than as a tool to replace yourself!

## Anti-Patterns to Avoid

The following anti-patterns shall be avoided. Ask if you have a question about any of these. Unless specified elsewhere, each occurrence of these anti-patterns will result in a **two point deduction** so please be careful!

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


