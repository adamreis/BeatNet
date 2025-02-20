"""
Created 07-01-21 by Mojtaba Heydari <mheydari@ur.rochester.edu>
"""

import setuptools
from setuptools import find_packages
import distutils.cmd

REQUIRED_PACKAGES = [
    "numpy",
    "cython",
    "librosa>=0.10.1",
    "numba>=0.58.1",
    "scipy",
    "mido>=1.2.6",
    "pytest",
    "madmom",
    "torch",
    "Matplotlib"
]

class MakeReqsCommand(distutils.cmd.Command):
    """A custom command to export requirements to a requirements.txt file."""
    description = "Export requirements to a requirements.txt file."
    user_options = []

    def initialize_options(self):
        """Set default values for options."""
        pass

    def finalize_options(self):
        """Post-process options."""
        pass

    def run(self):
        """Run command."""
        with open("./requirements.txt", "w") as f:
            for req in REQUIRED_PACKAGES:
                f.write(req)
                f.write("\n")

setuptools.setup(
    cmdclass={
        "make_reqs": MakeReqsCommand
    },
    name="BeatNet",
    version="1.1.3",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    install_requires=REQUIRED_PACKAGES,
    author="Mojtaba Heydari",
    author_email="mheydari@ur.rochester.edu",
    description="A package for Real-time and offline music beat, downbeat, tempo and meter tracking using BeatNet AI",
    keywords="Beat tracking, Downbeat tracking, meter detection, tempo tracking, particle filtering, real-time beat, real-time tempo",
    url="https://github.com/mjhydri/BeatNet"
)
