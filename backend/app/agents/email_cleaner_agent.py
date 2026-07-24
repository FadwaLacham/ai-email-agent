from bs4 import BeautifulSoup
import re


class EmailCleanerAgent:


    def clean_html(self, text):

        soup = BeautifulSoup(
            text,
            "html.parser"
        )

        return soup.get_text(
            separator=" "
        )


    def remove_urls(self, text):

        return re.sub(
            r"https?://\S+",
            "",
            text
        )


    def remove_extra_spaces(self, text):

        return re.sub(
            r"\s+",
            " ",
            text
        ).strip()


    def remove_email_footer(self, text):

        keywords = [
            "unsubscribe",
            "manage your alerts",
            "do not reply",
            "privacy policy"
        ]

        lower_text = text.lower()


        for keyword in keywords:

            index = lower_text.find(keyword)

            if index != -1:

                text = text[:index]


        return text.strip()



    def clean(self, email):

        body = email["body"]


        body = self.clean_html(
            body
        )


        body = self.remove_urls(
            body
        )


        body = self.remove_email_footer(
            body
        )


        body = self.remove_extra_spaces(
            body
        )


        email["clean_body"] = body


        return email