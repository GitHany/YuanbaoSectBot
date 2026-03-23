"""
YuanbaoSectBot 项目配置文件
"""

from setuptools import setup, find_packages

setup(
    name="yuanbaosectbot",
    version="1.0.0",
    description="Python算法库，包含常见算法的详细实现",
    author="GitHany",
    author_email="",
    url="https://github.com/GitHany/YuanbaoSectBot",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
)