# Copyright Amazon.com, Inc. or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
import setuptools

with open("readme.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aft-common",
    version="0.1.0",
    author="AWS",
    description="Common framework for AWS Control Tower Account Factory for Terraform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aws-ia/terraform-aws-control_tower_account_factory",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    package_data={"aft_common": ["schemas/*.json"]},
    python_requires=">=3.8",
    install_requires=[
        "appdirs==1.4.4",
        "attrs==21.2.0",
        "autopep8==1.5.7",
        "boto3==1.24.23",
        "botocore==1.27.23",
        "cffi==1.14.6",
        "cryptography == 3.4.7",
        "decorator == 5.0.9",
        "distlib == 0.3.2",
        "execnet == 1.9.0",
        "filelock == 3.0.12",
        "git-remote-codecommit == 1.15.1",
        "iniconfig == 1.1.1",
        "jsonpath == 0.82",
        "jsonpath-ng == 1.5.3",
        "lark-parser == 0.10.1",
        "packaging == 20.9",
        "pluggy == 0.13.1",
        "ply == 3.11",
        "py == 1.10.0",
        "pycparser == 2.20",
        "Pygments == 2.10.0",
        "pyparsing == 2.4.7",
        "pyrsistent == 0.17.3",
        "python-dateutil == 2.8.1",
        "python-hcl2 == 3.0.1",
        "python-terraform == 0.10.1",
        "pytz == 2021.1",
        "PyYAML == 5.4.1",
        "regex == 2021.8.3",
        "six == 1.16.0",
        "toml == 0.10.2",
        "tzlocal == 2.1",
        "urllib3 == 1.26.5",
        "utils == 1.0.1",
        "virtualenv == 20.4.7",
        "wcwidth == 0.2.5",
        "whaaaaat == 0.5.2",
        "Jinja2 == 3.1.3",
        "jsonschema == 4.3.2",
        "requests == 2.28.0",
    ],
    extras_require={
        "dev": [
            "pytest == 7.1.2",
            "pytest-subtests == 0.8.0",
            "ipython == 8.4.0",
            "ipdb == 0.13.9",
            "black == 22.6.0",
            "isort == 5.10.1",
            "click == 8.0.4",
            "checkov == 2.0.694",
            "pre-commit == 2.19.0",
            "mypy == 0.961",
            "boto3-stubs[support, stepfunctions, ec2, organizations, servicecatalog, sqs, lambda, sns, sts, cloudtrail, ssm, iam, dynamodb] == 1.24.22",
            "aws_lambda_powertools == 1.25.9",
            "autoflake == 1.4",
            "prospector == 1.7.7",
            "types-requests == 2.27.5",
        ]
    },
)
