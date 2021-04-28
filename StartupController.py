import pandas as pd
import numpy as np


class StartupController:
    def __init__(self):
        self.companies = pd.read_csv('objects.csv', low_memory=False)

        self.companies.drop(["created_at", "updated_at", "logo_url", "logo_width", "overview", "entity_id",
                             "parent_id", "normalized_name", "logo_height", "short_description", "created_at",
                             "updated_at", "twitter_username", "relationships", "domain", "homepage_url",
                             "overview", "tag_list", "state_code", "permalink", "first_investment_at",
                             "last_investment_at",
                             "first_milestone_at", "last_milestone_at", "milestones", "investment_rounds",
                             "invested_companies",
                             "first_funding_at", "last_funding_at", "funding_rounds"], axis="columns", inplace=True)

    def all_companies_name(self):
        return self.companies['name'].drop_duplicates().to_json(orient="records")

    def all_statuses(self):
        return self.companies['status'].drop_duplicates().to_json(orient="records")

    def hello(self):
        return "hello"
