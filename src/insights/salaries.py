from typing import Union, List, Dict

import src.insights.jobs as jobs


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    try:
        top_salary = 0
        list = jobs.read(path)

        for offer in list:
            salary = offer["max_salary"]
            if salary > top_salary and salary != "":
                top_salary = salary
    except NotImplementedError:
        raise NotImplementedError
    else:
        return round(top_salary)


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    try:
        min_salary = get_max_salary(path)
        list = jobs.read(path)

        for offer in list:
            salary = offer["min_salary"]
            if salary < min_salary and salary != "":
                min_salary = salary
    except NotImplementedError:
        raise NotImplementedError
    else:
        return round(min_salary)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    try:
        min = int(job["min_salary"])
        max = int(job["max_salary"])
        if max > min:
            return salary >= min and salary <= max
    except ValueError:
        ValueError()


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    try:
        list = []
        for offer in jobs:
            if matches_salary_range(offer, salary):
                list.append(offer)
    except ValueError:
        ValueError()
