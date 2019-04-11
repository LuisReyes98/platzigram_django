#!/usr/bin/env python
import os
import sys

# ALL the machine learning libraries are available in python3 as well
# import sklearn as sk
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sb


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'platzigram.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
