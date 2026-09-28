"""
All of your site's content lives here.
Edit the values below, save, and refresh the page — no HTML needed.
Leave a list empty ([]) to hide that section.
"""

SITE = {
    "name": "Michelle Wang",
    "title": "Data Science & Machine Learning",
    "tagline": "I build data and AI solutions, and I love bridging the gap between business and technology.",
    "email": "michellewang0402@gmail.com",
    # Small badge under your summary (set to None to hide)
    "status": "Open to new opportunities",
    # Shown in the Contact section at the bottom of the page
    "contact_heading": "Open to data science and machine learning roles.",
    "contact_message": "I'm interested in opportunities in data science, machine learning, and AI "
                       "engineering. If you're hiring for a role that could be a fit, I'd love to connect. "
                       "Feel free to reach out by email.",
    # Put your resume at static/resume.pdf, or set to None to hide the button
    "resume": "resume.pdf",
}

LINKS = [
    {"label": "GitHub", "url": "https://github.com/wangmichelle1"},
    {"label": "LinkedIn", "url": "https://www.linkedin.com/in/michelle-wang-b0a917107"},
    {"label": "Tableau", "url": "https://public.tableau.com/app/profile/michelle.wang3592"},
]

ABOUT = """
I'm interested in anything data related, from building machine learning models and AI agents to
designing databases and dashboards. I'm currently a Technology Analyst II on the Data Science/Machine
Learning team at Fiserv, where I build agentic AI chatbots, ML models, and automated reporting pipelines.

I studied Data Science and Business Administration at Northeastern University, so I'm just as comfortable
writing code as I am turning data into decisions for business stakeholders. I enjoy development roles
as well as roles that bridge the gap between the business and technical sides of a team.

In my free time, I like to do 1000-piece jigsaw puzzles, build miniature houses, collect blind boxes,
and watch horror and rom-com shows and movies.
"""

# Quick highlights shown under the About section
STATS = [
    {"value": "3.95", "label": "GPA at Northeastern"},
    {"value": "4", "label": "Data & ML roles"},
    {"value": "8", "label": "Data projects"},
]

EXPERIENCE = [
    {
        "role": "Technology Analyst II, Data Science/Machine Learning",
        "company": "Fiserv",
        "dates": "June 2025 – Present",
        "location": "Berkeley Heights, NJ",
        "bullets": [
            "Design and implement a chatbot using the Semantic Kernel framework, with a Router Agent and 20+ specialized "
            "Azure AI Foundry agents (plus generic plugins), Azure AI Search that chooses traditional or hybrid search "
            "based on the prompt, and thread-based conversation history to preserve context for change managers’ queries.",
            "Build and maintain end-to-end lifecycle APIs for Azure AI Foundry agents (creation, update, deletion), with "
            "HMAC-secured authorization flows and role-based permissions to secure access to the chatbot and its plugins.",
            "Engineer and iteratively refine ML models using data from MongoDB and PostgreSQL, working with product "
            "managers to optimize performance and deliver insights for proactive risk mitigation.",
            "Develop an automated pipeline with Python, Crontab, and Azure Communication Services that generates 4+ daily "
            "reports of visualizations and KPI summaries on release readiness and change-driven incidents, giving "
            "leadership data and LLM-based insights to evaluate process effectiveness.",
        ],
    },
    {
        "role": "Research Data Analyst Co-op",
        "company": "GMO LLC",
        "dates": "Aug 2024 – Dec 2024",
        "location": "Boston, MA",
        "bullets": [
            "Maintained robust, scalable SQL databases in Microsoft SQL Server to enhance investment processes, "
            "collaborating with investment teams and external market data vendors.",
            "Developed automated Python scripts for data validation, proactively identifying and resolving "
            "inconsistencies to ensure data accuracy.",
        ],
    },
    {
        "role": "Internet Data Analyst Intern",
        "company": "Lumen Technologies",
        "dates": "May 2024 – Aug 2024",
        "location": "Remote",
        "bullets": [
            "Compared trends in CDR and Rate/Mbps for High Speed IP Billing Arrangements, traffic, and revenue using 4+ "
            "Tableau visualizations, uncovering missed high-margin customer opportunities and driving product managers "
            "to shift toward those segments.",
        ],
    },
    {
        "role": "Machine Intelligence Co-op",
        "company": "Draper Laboratory",
        "dates": "July 2023 – Jan 2024",
        "location": "Cambridge, MA",
        "bullets": [
            "Engineered 8+ ML classification algorithms (e.g., linear discriminant analysis, neural networks) and 4+ "
            "feature selection methods (e.g., ANOVA, lasso) in Python and MATLAB for predictive maintenance of accelerometers.",
            "Built a Plotly Dash web app with 5+ interactive expenditure visualizations and automated Excel exports via a "
            "Selenium batch script, streamlining reporting and reducing manual effort for the Finance team.",
        ],
    },
]

# "category" powers the filter buttons (keep to ~3 categories).
# "link" is optional: add a GitHub/demo URL to make the card clickable.
# "slug", "problem", "approach", "results" power each project's case-study page.
# Optional "image": put a chart/screenshot in static/projects/ and set e.g.
#   "image": "projects/sleep-dashboard.png", "image_caption": "The Snoozeless dashboard"
PROJECTS = [
    {
        "name": "Emotional Intelligence Coach",
        "category": "AI & ML",
        "description": "An agentic AI application built on an Ollama LLM that helps employees communicate "
                       "with greater emotional intelligence in the workplace.",
        "tech": ["Agentic AI", "Ollama", "Python"],
        "link": None,
        "slug": "emotional-intelligence-coach",
        "problem": "Communicating with empathy and self-awareness is a big part of working well together, but employees rarely get feedback on the emotional side of how they communicate.",
        "approach": [
            "Built an agentic AI application powered by an Ollama LLM.",
            "Designed the agent to coach employees toward more emotionally intelligent workplace communication.",
        ],
        "results": [
            "A working AI coaching app aimed at improving communication between employees, and in turn creating value for the company.",
        ],
    },
    {
        "name": "Identifying AI-Generated Text",
        "category": "AI & ML",
        "description": "Preprocessed 500k labeled essays (cleaning, lemmatization, undersampling, TF-IDF) and "
                       "trained 4+ models to predict whether an essay was written by AI or a human.",
        "tech": ["Python", "NLP", "Logistic Regression", "Gradient Boosting", "LSTM"],
        "link": "https://github.com/wangmichelle1/DS4400Project",
        "slug": "ai-generated-text",
        "problem": "As AI writing tools become common, it's getting harder to tell whether an essay was written by a person or generated by AI.",
        "approach": [
            "Explored a dataset of 500k essays labeled as AI-generated or human-written.",
            "Preprocessed the text with cleaning, lemmatization, and TF-IDF vectorization, and used undersampling to balance the classes.",
            "Trained and compared a suite of models: logistic regression, decision tree, random forest, gradient boosting, and an LSTM.",
        ],
        "results": [
            "Built an end-to-end NLP pipeline, from raw essays to trained classifiers, that predicts whether an essay is AI-generated or human-written.",
            "Compared classical ML and deep learning approaches on the same data.",
        ],
    },
    {
        "name": "ADHD Diagnosis & Heart Rate Variability",
        "category": "AI & ML",
        "description": "Neural networks in R (Torch) predicting ADHD with ~60% accuracy, plus autoregressive and "
                       "moving-average time series models built from scratch in Python to forecast heart rate variability.",
        "tech": ["R", "Torch", "Python", "Time Series"],
        "link": "https://github.com/wangmichelle1/DS-4420-Final-Project",
        "slug": "adhd-heart-rate-variability",
        "problem": "Can physiological signals like heart rate help identify ADHD and reveal patterns in how patients' bodies behave?",
        "approach": [
            "Cleaned the patient dataset and converted raw heart rate readings into heart rate variability (HRV) data.",
            "Built neural networks in R with the Torch package to predict ADHD, tuning hyperparameters to find the best configuration.",
            "Implemented autoregressive (AR) and moving average (MA) time series models from scratch in Python to forecast HRV for individual patients.",
        ],
        "results": [
            "The best neural network reached about 60% accuracy in predicting ADHD.",
            "The time series models forecast HRV and gave insight into physiological patterns in patients with ADHD.",
        ],
    },
    {
        "name": "Universal Music Database System",
        "category": "Databases",
        "description": "A MySQL database with relational schemas, stored procedures, and triggers, plus a Python CLI "
                       "where users authenticate, manage streaming preferences, run CRUD on songs/artists/albums/reviews, "
                       "and view personalized activity stats.",
        "tech": ["MySQL", "Python", "SQL"],
        "link": "https://github.com/wangmichelle1/Universal-music-database-system",
        "slug": "universal-music-database",
        "team": True,
        "problem": "Listeners use different streaming services, but there's no single place to search music and share reviews across them.",
        "approach": [
            "Designed a MySQL database with relational schemas, stored procedures, and triggers.",
            "Built a Python command-line app using MySQL connectors so users can create an account and choose their streaming services.",
            "Added search across artists, songs, albums, and their reviews, plus creating, updating, and deleting reviews.",
        ],
        "results": [
            "Permissions ensure users can only edit or delete their own reviews.",
            "Users can view personal activity stats (searches and reviews) and see how many users are on each streaming service.",
        ],
    },
    {
        "name": "Manhattan Rent Price Prediction",
        "category": "Analytics",
        "description": "Explanatory models in Python, Tableau, and Excel on what drives Manhattan rents, and predictive "
                       "models (KNN, multiple linear, random forest) reaching r² > 0.80.",
        "tech": ["Python", "Scikit-Learn", "Tableau", "Excel"],
        "link": "https://github.com/wangmichelle1/Manhattan-rent-price-prediction",
        "slug": "manhattan-rent-prediction",
        "problem": "About 67% of New Yorkers rent (as of May 2022), and Manhattan rents are especially high. The goal was to help renters understand what drives price and get the best place for their budget.",
        "approach": [
            "Built explanatory models in Excel, Python, and Tableau to analyze how different factors relate to rent.",
            "Used a random forest to identify the most important factors.",
            "Trained predictive models in Python (k-nearest neighbors, multiple linear regression, and random forest) on those factors.",
        ],
        "results": [
            "The predictive models reached r² > 0.80.",
        ],
    },
    {
        "name": "Sleep Efficiency Dashboard",
        "category": "Analytics",
        "description": "An interactive Plotly Dash dashboard combining Python ML algorithms and 6+ visualizations to "
                       "help users analyze sleep patterns and how lifestyle habits affect sleep quality.",
        "tech": ["Python", "Plotly Dash", "Machine Learning"],
        "link": "https://github.com/wangmichelle1/Sleep-Efficiency",
        "slug": "sleep-efficiency-dashboard",
        "problem": "Most people know sleep matters, but it's hard to see which habits actually affect sleep quality.",
        "approach": [
            "Built Snoozeless, an interactive dashboard in Plotly Dash with dropdowns and sliders.",
            "Included 6+ visualizations, from scatter plots and histograms to a density contour plot and a radar chart.",
            "Integrated a machine learning model where users enter their bedtime, sleep duration, caffeine intake, and exercise to see stats about their sleep quality.",
        ],
        "results": [
            "Supported the hypothesis that sleeping longer, less caffeine and alcohol, not smoking, and more exercise improve sleep quality.",
            "Found that gender plays a minimal direct role, while age, how often you wake up, and alcohol consumption have a major effect.",
        ],
    },
    {
        "name": "Breast Cancer Survival Analysis",
        "category": "AI & ML",
        "description": "Predicted years of survival after diagnosis from Netherlands Cancer Institute patient data "
                       "(273 × 1570) using KNN, decision trees, random forests, PCA, and multiple regression.",
        "tech": ["Python", "Scikit-Learn", "PCA"],
        "link": "https://github.com/wangmichelle1/Breast-Cancer-Survival-Analysis",
        "slug": "breast-cancer-survival",
        "problem": "Could patient data like age, tumor grade, and protein expression predict how many years a breast cancer patient survives after diagnosis?",
        "approach": [
            "Used Netherlands Cancer Institute patient data (273 patients × 1,570 features).",
            "Built k-nearest neighbors, decision tree, random forest, PCA, and multiple regression models.",
        ],
        "results": [
            "Multiple regression on protein expression levels performed best.",
            "All of the models showed weak relationships between the features and survival, so they shouldn't be used for real predictions. Knowing a model's limits is part of the result.",
        ],
    },
    {
        "name": "Good2Go Unsupervised Learning",
        "category": "Analytics",
        "description": "K-means clustering of active members, visualized with silhouette and cluster plots, leading "
                       "to 5+ business recommendations to improve engagement and retention.",
        "tech": ["K-Means", "Clustering", "Data Visualization"],
        "link": None,
        "slug": "good2go-clustering",
        "problem": "Good2Go wanted to understand its active members better in order to improve engagement and retention.",
        "approach": [
            "Applied K-means clustering to find natural groupings among active members.",
            "Evaluated and visualized the clusters with silhouette plots and cluster plots.",
        ],
        "results": [
            "Delivered 5+ actionable business recommendations, such as targeted promotions encouraging frequent short-distance renters to book longer trips.",
        ],
    },
]

EDUCATION = [
    {
        "school": "Northeastern University",
        "degree": "B.S. in Data Science and Business Administration (Business Analytics)",
        "dates": "April 2025",
        "location": "Boston, MA",
        "details": "GPA: 3.95 / 4.00",
        "coursework": "Machine Learning/Data Mining II, Large-Scale Storage, Modeling for Business Analytics, "
                      "Database Design, Fundamentals of Information Analytics, Creating Business Value with "
                      "Data and AI Tech, Information Visualization, Probability & Statistics",
        "activities": "Club Management Lead of Khoury College Club Council, Vice President of DATA Club, "
                      "Volunteer at Circle K",
    },
]

SKILLS = {
    "Data Skills": ["Agentic AI", "Machine Learning", "Data Analysis", "Data Visualization",
                    "Database Management", "Quality Assurance"],
    "Languages": ["Python", "SQL", "R", "JavaScript", "HTML", "CSS", "MATLAB"],
    "Databases": ["PostgreSQL", "MySQL", "SQL Server", "Oracle", "MongoDB", "Redis", "Neo4j"],
    "ML & Data Libraries": ["Scikit-Learn", "Pandas", "NumPy", "Keras", "Matplotlib", "Seaborn"],
    "Visualization": ["Tableau", "Power BI", "Plotly Dash"],
    "Tools & Platforms": ["Azure AI Foundry", "Databricks", "Git", "Jira", "Postman", "Jupyter",
                          "Visual Studio", "PyCharm", "Excel", "PowerPoint"],
}
