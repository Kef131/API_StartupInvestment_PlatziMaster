import pandas as pd

data = {
    'apples': [3, 2, 0, 1],
    'oranges': [0, 3, 7, 2]
}

purchases = pd.DataFrame(data)

print(purchases)

purchases = pd.DataFrame(data, index=['June', 'Robert', 'Lily', 'David'])

print(purchases)

print(purchases.loc['June'])

companies = pd.read_csv('DataSet_StartupInvestment/objects.csv', low_memory=False)

print(companies.head())
print(companies.dtypes)
print(companies['entity_type'].value_counts())
print(companies['status'].value_counts())

companies.drop(["updated_at", "logo_url", "logo_width","overview", "entity_id","parent_id","normalized_name", "logo_height","short_description", "twitter_username","relationships", "domain", "homepage_url", "tag_list", "state_code"], axis="columns", inplace=True)
companies.info()