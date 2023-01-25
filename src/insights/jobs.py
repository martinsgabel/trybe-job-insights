from functools import lru_cache
from typing import List, Dict

import csv


@lru_cache
def read(path: str) -> List[Dict]:
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    dict_res = []
    try:
        with open(path, mode="r") as file:
            cvs_file = csv.DictReader(file)
            for line in cvs_file:
                dict_res.append(line)
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo {path} não encontrado")
    else:
        return dict_res


def get_unique_job_types(path: str) -> List[str]:
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    try:
        job_type_list = []
        list = read(path)
        for offer in list:
            title = offer["job_title"]
            if title != '' and title not in job_type_list:
                job_type_list.append(title)
        return job_type_list[4]
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo {path} não encontrado")


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
