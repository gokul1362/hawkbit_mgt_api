# coding: utf-8

"""
    hawkBit REST APIs

    Eclipse hawkBit™ is a domain-independent back-end framework for rolling out software updates to constrained edge devices as well as more powerful controllers and gateways connected to IP based networking infrastructure.   # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class SoftwareModuleTypesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_software_module_types(self, body, **kwargs):  # noqa: E501
        """Creates new Software Module Types  # noqa: E501

        Handles the POST request of creating new software module types. The request body must always be a list of module types. Required Permission: CREATE_REPOSITORY  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_software_module_types(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[MgmtSoftwareModuleTypeRequestBodyPost] body: (required)
        :return: list[MgmtSoftwareModuleType]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_software_module_types_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_software_module_types_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_software_module_types_with_http_info(self, body, **kwargs):  # noqa: E501
        """Creates new Software Module Types  # noqa: E501

        Handles the POST request of creating new software module types. The request body must always be a list of module types. Required Permission: CREATE_REPOSITORY  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_software_module_types_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[MgmtSoftwareModuleTypeRequestBodyPost] body: (required)
        :return: list[MgmtSoftwareModuleType]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_software_module_types" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_software_module_types`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/hal+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/hal+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/rest/v1/softwaremoduletypes', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[MgmtSoftwareModuleType]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_software_module_type(self, software_module_type_id, **kwargs):  # noqa: E501
        """Delete Software Module Type by Id  # noqa: E501

        Handles the DELETE request for a single software module type. Required Permission: DELETE_REPOSITORY  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_software_module_type(software_module_type_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int software_module_type_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_software_module_type_with_http_info(software_module_type_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_software_module_type_with_http_info(software_module_type_id, **kwargs)  # noqa: E501
            return data

    def delete_software_module_type_with_http_info(self, software_module_type_id, **kwargs):  # noqa: E501
        """Delete Software Module Type by Id  # noqa: E501

        Handles the DELETE request for a single software module type. Required Permission: DELETE_REPOSITORY  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_software_module_type_with_http_info(software_module_type_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int software_module_type_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['software_module_type_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_software_module_type" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'software_module_type_id' is set
        if ('software_module_type_id' not in params or
                params['software_module_type_id'] is None):
            raise ValueError("Missing the required parameter `software_module_type_id` when calling `delete_software_module_type`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'software_module_type_id' in params:
            path_params['softwareModuleTypeId'] = params['software_module_type_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/rest/v1/softwaremoduletypes/{softwareModuleTypeId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_software_module_type(self, software_module_type_id, **kwargs):  # noqa: E501
        """Return single Software Module Type  # noqa: E501

        Handles the GET request of retrieving a single software module type. Required Permission: READ_REPOSITORY  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_software_module_type(software_module_type_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int software_module_type_id: (required)
        :return: MgmtSoftwareModuleType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_software_module_type_with_http_info(software_module_type_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_software_module_type_with_http_info(software_module_type_id, **kwargs)  # noqa: E501
            return data

    def get_software_module_type_with_http_info(self, software_module_type_id, **kwargs):  # noqa: E501
        """Return single Software Module Type  # noqa: E501

        Handles the GET request of retrieving a single software module type. Required Permission: READ_REPOSITORY  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_software_module_type_with_http_info(software_module_type_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int software_module_type_id: (required)
        :return: MgmtSoftwareModuleType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['software_module_type_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_software_module_type" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'software_module_type_id' is set
        if ('software_module_type_id' not in params or
                params['software_module_type_id'] is None):
            raise ValueError("Missing the required parameter `software_module_type_id` when calling `get_software_module_type`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'software_module_type_id' in params:
            path_params['softwareModuleTypeId'] = params['software_module_type_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/hal+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/rest/v1/softwaremoduletypes/{softwareModuleTypeId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MgmtSoftwareModuleType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_types(self, **kwargs):  # noqa: E501
        """Return all Software Module Types  # noqa: E501

        Handles the GET request of retrieving all software module types. Required Permission: READ_REPOSITORY  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_types(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str offset: The paging offset (default is 0)
        :param str limit: The maximum number of entries in a page (default is 50)
        :param str sort: The query parameter sort allows to define the sort order for the result of a query. A sort criteria consists of the name of a field and the sort direction (ASC for ascending and DESC descending). The sequence of the sort criteria (multiple can be used) defines the sort order of the entities in the result.
        :param str q: Query fields based on the Feed Item Query Language (FIQL). See Entity Definitions for available fields.
        :return: PagedListMgmtSoftwareModuleType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_types_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_types_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_types_with_http_info(self, **kwargs):  # noqa: E501
        """Return all Software Module Types  # noqa: E501

        Handles the GET request of retrieving all software module types. Required Permission: READ_REPOSITORY  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_types_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str offset: The paging offset (default is 0)
        :param str limit: The maximum number of entries in a page (default is 50)
        :param str sort: The query parameter sort allows to define the sort order for the result of a query. A sort criteria consists of the name of a field and the sort direction (ASC for ascending and DESC descending). The sequence of the sort criteria (multiple can be used) defines the sort order of the entities in the result.
        :param str q: Query fields based on the Feed Item Query Language (FIQL). See Entity Definitions for available fields.
        :return: PagedListMgmtSoftwareModuleType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['offset', 'limit', 'sort', 'q']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_types" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'q' in params:
            query_params.append(('q', params['q']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/hal+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/rest/v1/softwaremoduletypes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PagedListMgmtSoftwareModuleType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_software_module_type(self, body, software_module_type_id, **kwargs):  # noqa: E501
        """Update Software Module Type  # noqa: E501

        Handles the PUT request for a single software module type. Required Permission: UPDATE_REPOSITORY  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_software_module_type(body, software_module_type_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MgmtSoftwareModuleTypeRequestBodyPut body: (required)
        :param int software_module_type_id: (required)
        :return: MgmtSoftwareModuleType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_software_module_type_with_http_info(body, software_module_type_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_software_module_type_with_http_info(body, software_module_type_id, **kwargs)  # noqa: E501
            return data

    def update_software_module_type_with_http_info(self, body, software_module_type_id, **kwargs):  # noqa: E501
        """Update Software Module Type  # noqa: E501

        Handles the PUT request for a single software module type. Required Permission: UPDATE_REPOSITORY  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_software_module_type_with_http_info(body, software_module_type_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MgmtSoftwareModuleTypeRequestBodyPut body: (required)
        :param int software_module_type_id: (required)
        :return: MgmtSoftwareModuleType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'software_module_type_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_software_module_type" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_software_module_type`")  # noqa: E501
        # verify the required parameter 'software_module_type_id' is set
        if ('software_module_type_id' not in params or
                params['software_module_type_id'] is None):
            raise ValueError("Missing the required parameter `software_module_type_id` when calling `update_software_module_type`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'software_module_type_id' in params:
            path_params['softwareModuleTypeId'] = params['software_module_type_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/hal+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/hal+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/rest/v1/softwaremoduletypes/{softwareModuleTypeId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MgmtSoftwareModuleType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
