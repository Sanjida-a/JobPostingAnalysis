import pandas as pd
import random

# replace with dummy values
df = pd.read_csv('master.csv')
df['Organization Name'] = 'Organization_' + (df.index + 1).astype(str)
df['Position'] = df['Position'].apply(lambda x: f"Position_{random.randint(1, 100)}")
df['Country'] = 'Country_' + (df.index + 1).astype(str)
df['Job ID'] = df['Job ID'].apply(lambda x: f"JobID_{random.randint(1, 1000)}")

# delete unwanted columns
columns_to_keep = [
    'Job ID', 'Position', 'Posting Status', 'Date Created', 'Application Deadline', 'Reposted',
    'Term Posted', 'Number of Positions', 'All Degrees and Disciplines', 'Salary Range', 'Duration',
    'Application Delivery Method', 'Application Procedure', 'Skills and Qualifications', 
    'Duties and Responsibilities', 'Work Type', 'Work Location (City, Province)', 'Organization Name', 
    'Country', 'Total View Count', 'Unique View Count', 'Application Count', 'Selected for Interview Count', 
    'Placement Records Count'
]
df = df[columns_to_keep]
df.to_csv('cleaned_job_postings.csv', index=False)
