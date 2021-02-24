# =================================================================
# Class_Ex1:
# We will be working with a famous titanic data set for these exercises.
# Later on in the Data mining section of the course, we will work  this data,
# and use it to predict survival rates of passengers.
# For now, we'll just focus on the visualization of the data with seaborn:

# use seaborn to load dataset
# ----------------------------------------------------------------
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style('whitegrid')
titanic = sns.load_dataset('titanic')

# =================================================================
# Class_Ex2:
# Join plot on fare and age
# ----------------------------------------------------------------

sns.jointplot(titanic['age'], titanic['fare'])
plt.show()



# =================================================================
# Class_Ex3:
# Distribution plot on fare with red color and 35 bin
# ----------------------------------------------------------------

sns.distplot(titanic['fare'], bins = 35, color = 'r')
plt.show()

# =================================================================
# Class_Ex4:
# box plot on class and age
# ----------------------------------------------------------------

sns.boxplot(titanic['class'], titanic['age'])
plt.show()

# =================================================================
# Class_Ex5:
# swarmplot on class and age
# ----------------------------------------------------------------

sns.swarmplot(titanic['class'], titanic['age'])
plt.show()


# =================================================================
# Class_Ex6:
# Count plot on sex
# ----------------------------------------------------------------

sns.countplot(titanic['sex'])
plt.show()


# =================================================================
# Class_Ex7:
# plot heatmap
# ----------------------------------------------------------------

TP = titanic.pivot_table('survived', index='sex', columns='class')
sns.heatmap(TP, annot=True)
plt.show()




# =================================================================
# Class_Ex8:
# Distribution of male and female ages in same grapgh (Facet)
# ----------------------------------------------------------------

FG = sns.FacetGrid(titanic, col = 'sex')
FG.map(plt.hist, 'age')
plt.show()




# =================================================================
# Class_Ex9:
# Explain each graph and describe the results in words
# ----------------------------------------------------------------

# Joint plot: The joint plot shows the scattered distribution of age and fare and the relationship
# between the two. For most passengers, regardless of age, the fare was between 0 and 100, but we
# see that some individuals in the age range of 10 and 70 had fares ranging from 100 to 375.

# Dist: The distribution plot shows the frequency that each fare amount occurs along with the
# distribution. We see that distribution is right skewed with the mean fare being ~30 with fares
# ranging from 0 to ~575.

# Box plot: The box plot on class and age shows a five number summary for age versus class.
# The average age is highest in first class and decreases in descending order of class.
# First class passengers range from age 0 to 80 with a mean of ~ 38, second class range from 0 to ~72
# with a mean of ~29, and third range from 0 to ~75 with a mean of ~24.

# Swarm plot: The swarm plot shows all observations and underlying distribution for age versus class.
# Our plot shows that most first class passengers fall between ages 15 and 65, most second class passengers
# fall between ages 19 and 38, and most third class passengers fall between ages 15 and 35.

# Count plot: The count plot on sex shows the number of male and female passengers aboard the ship.
# There were ~575 male passengers and ~315 female passengers.

# Heatmap: The heat map shows the survival rate of passengers by sex and class. We see that women
# of every class had a higher survival rate than men of any class, with first class women having
# the highest survival rate (97%) and third class men having the lowest survival rate (14%).

# Facet: The facet grid shows the distribution of both women and men passengers by age separately on
# the same graph. We see that the majority of men are between the ages of 20 and 40 and the distribution
# is right skewed, while the majority of women are between the ages of 15 and 35 and the distribution is
# slightly right skewed as well.





