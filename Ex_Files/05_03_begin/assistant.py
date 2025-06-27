import os
from openai import OpenAI # python -m pip install openai
# python -m pip install pipupgrade
# install the PipUpgrade package, which automates the process of updating all your Python packages across various environments.

# 1. python -m pip install pipupgrade
# This command attempts to install a package named pipupgrade. This package is a third-party tool designed to simplify the process of upgrading all installed pip packages in a Python environment.
# Purpose: It is used specifically for upgrading pip-installed packages to their latest versions efficiently in one command.
# Installation: If pipupgrade is not already installed, this command will download and install it. If it is already installed, it will check for an update.
# 2. python -m pip install --upgrade pip
# This command upgrades pip itself to the latest version available from the Python Package Index (PyPI).
# Purpose: It specifically updates the pip tool that is used to manage packages. Keeping pip updated ensures access to the latest features, bug fixes, and improvements.
# Installation: If the installed version of pip is outdated, this command will replace it with the newer version.

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant who speaks in rhyme.",
        },
        {
            "role": "user",
            "content": "Who was Alexander Hamilton?",
        }
    ],
    model=model_name,
    temperature=1.0,
    max_tokens=1000,
    top_p=1.0
)

print(response.choices[0].message.content)