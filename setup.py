from setuptools import setup, find_packages

install_requires = [
    # "gurobipy",  	 # install this manually
    # "alib",      	 # install this manually
    # "vnep_approx", # install this manually
    "matplotlib",
    "numpy",
    "click",
    "pyyaml",
    "jsonpickle",
]

setup(
    name="evaluation-ifip-networking-2018",
    python_requires=">=3.7",
    packages=["evaluation_ifip_networking_2018"],
    install_requires=install_requires,
    entry_points={
        "console_scripts": [
            "evaluation-ifip-networking-2018 = evaluation_ifip_networking_2018.cli:cli",
        ]
    }
)
