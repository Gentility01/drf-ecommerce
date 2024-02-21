import logging  # Importing the logging module for logging messages.
import urllib.parse  # Importing the urllib.parse module for parsing URLs.
from collections import \
    OrderedDict  # Importing OrderedDict for creating ordered dictionaries.
from typing import (  # Importing Any and Literal types from the typing module for function annotations.
    Any, Literal)
from unittest.mock import \
    MagicMock  # Importing MagicMock from the unittest.mock module for creating mock objects.

from django.utils import timezone  # Importing timezone utilities from Django.


class TestHelper:  # Defining a class named TestHelper for providing helper methods for testing.
    def add_permission_side_effect(self, mock_dependency: MagicMock, permission: dict[str, Any]) -> MagicMock:
        """
        Sets the side effect for the given mock_dependency to return the permission value based on the dot_path in the permission dictionary.

        Args:
            mock_dependency (MagicMock): The mock dependency to set the side effect for.
            permission (dict[str, Any]): The permission dictionary containing the dot_path keys and their corresponding values.

        Returns:
            MagicMock: The updated mock_dependency with the side effect set.
        """
        mock_dependency.side_effect = lambda base_url, service, permission_id, dot_path: permission.get(dot_path)
        return mock_dependency  # Returning the modified mock_dependency object.

    def generate_timedelta(
        self,
        when: Literal["before", "after"],
        period: Literal["weeks", "days", "minutes", "seconds"] = "days",
        value: int = 2,
    ) -> str:
        """
        Args:
            when (Literal["before", "after"]): description
            period (Literal["weeks", "days", "minutes", "seconds"]): description
            value (int): description
        """
        if when == "before":
            return (timezone.now() - timezone.timedelta(**{period: value})).date().isoformat()
        elif when == "after":
            return (timezone.now() + timezone.timedelta(**{period: value})).date().isoformat()

    def no_duplicate(self, data: list[str | int] | list[dict[str, Any]], id_field: str | int = "id") -> bool:
        """
        Check for duplicates in the given data list or list of dictionaries based on the specified id field.

        Args:
            data (list[str | int] | list[dict[str, Any]]): The input data to check for duplicates.
            id_field (str | int, optional): The field to use as the identifier for each item in the data list of dictionaries. Defaults to "id".

        Returns:
            bool: True if there are no duplicates, False otherwise.
        """
        if not data:
            return True
        if type(data[0]) in [dict, OrderedDict]:
            data = [x.get(id_field) for x in data]
        return len(data) == len(set(data))

    def has_no_duplicate_in_response_results(self, response, id_field: str | int = "id") -> bool:
        """
        Check if there are any duplicate values in the response data based on the specified id field.

        Args:
            response: The response object containing the data to be checked.
            id_field (str | int): The field name or index to be used as the unique identifier. Defaults to "id".

        Returns:
            bool: True if there are no duplicate values, False otherwise.
        """
        data: list[str | int] | list[dict[str, Any]] = response.data.get("results")
        if not data:
            return True
        if type(data[0]) in [dict, OrderedDict]:
            data = [x.get(id_field) for x in data]
        return len(data) == len(set(data))

    def has_fields(self, response, fields: list[int | str]) -> bool:
        """
        Check if all fields are present in the response data.

        Args:
            response: The response object containing the data.
            fields: A list of field names or indices to check in the response data.

        Returns:
            bool: True if all fields are present in the response data, False otherwise.
        """
        data: dict = response.data
        conditions = []
        for x in fields:
            exist = x in data
            conditions.append(exist)
            if not exist:
                logging.warning("field -> '%s' does not exists", x)
        return all(conditions)

    def has_specified_fields(self, data, fields: list[int | str]) -> bool:
        conditions = []
        for x in fields:
            exist = x in data
            conditions.append(exist)
            if not exist:
                logging.warning("field -> '%s' does not exists", x)
        return all(conditions)

    def extract_results_in_response(self, response) -> list[dict]:
        return response.data.get("results")

    def has_fields_in_response_results(self, response, fields: list[int | str]) -> bool:
        results: list[dict] = response.data.get("results")
        if not results:
            return False
        data: dict = results[0]
        conditions = []
        for x in fields:
            exist = x in data
            conditions.append(exist)
            if not exist:
                logging.warning("field -> '%s' does not exists", x)
        return all(conditions)

    def has_paginated_count(self, response, count: int) -> bool:
        return response.data.get("count") == count

    def has_response_status(self, response, status_code: int) -> bool:
        return response.status_code == status_code

    def add_query_params_to_url(self, url: str, params: dict[str, Any]) -> str:
        query_string = urllib.parse.urlencode(params)
        return f"{url}?{query_string}"
