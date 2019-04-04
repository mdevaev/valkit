import setuptools


# =====
if __name__ == "__main__":
    setuptools.setup(
        name="valkit",
        version="0.1.4",
        url="https://github.com/mdevaev/valkit",
        license="LGPLv3",
        author="Devaev Maxim",
        author_email="mdevaev@gmail.com",
        description="Yet another Python validators",
        platforms="any",

        packages=[
            "valkit",
        ],

        classifiers=[  # http://pypi.python.org/pypi?:action=list_classifiers
            "Development Status :: 4 - Beta",
            "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
            "Programming Language :: Python :: 3",
            "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    )
