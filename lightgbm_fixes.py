# coding: utf-8
"""Compatibility library."""

from typing import Any, List

# scikit-learn imports
try:
    from sklearn.base import BaseEstimator, ClassifierMixin, RegressorMixin
    from sklearn.preprocessing import LabelEncoder
    from sklearn.utils.class_weight import compute_sample_weight
    from sklearn.utils.multiclass import check_classification_targets
    from sklearn.utils.validation import assert_all_finite, check_array, check_X_y

    try:
        from sklearn.exceptions import NotFittedError
        from sklearn.model_selection import BaseCrossValidator, GroupKFold, StratifiedKFold
    except ImportError:
        from sklearn.cross_validation import BaseCrossValidator, GroupKFold, StratifiedKFold
        from sklearn.utils.validation import NotFittedError

    try:
        from sklearn.utils.validation import _check_sample_weight
    except ImportError:
        from sklearn.utils.validation import check_consistent_length

        # Dummy function for older versions of scikit-learn
        def _check_sample_weight(sample_weight: Any, input_array: Any) -> Any:
            check_consistent_length(sample_weight, input_array)
            return sample_weight

    SKLEARN_INSTALLED = True
    _LGBMBaseCrossValidator = BaseCrossValidator
    _LGBMModelBase = BaseEstimator
    _LGBMRegressorBase = RegressorMixin
    _LGBMClassifierBase = ClassifierMixin
    _LGBMLabelEncoder = LabelEncoder
    LGBMNotFittedError = NotFittedError
    _LGBMStratifiedKFold = StratifiedKFold
    _LGBMGroupKFold = GroupKFold
    _LGBMCheckXY = check_X_y
    _LGBMCheckArray = check_array
    _LGBMCheckSampleWeight = _check_sample_weight
    _LGBMAssertAllFinite = assert_all_finite
    _LGBMCheckClassificationTargets = check_classification_targets
    _LGBMComputeSampleWeight = compute_sample_weight
except ImportError:
    SKLEARN_INSTALLED = False

    class _LGBMModelBase:  # type: ignore
        """Dummy class for sklearn.base.BaseEstimator."""
        pass

    class _LGBMClassifierBase:  # type: ignore
        """Dummy class for sklearn.base.ClassifierMixin."""
        pass

    class _LGBMRegressorBase:  # type: ignore
        """Dummy class for sklearn.base.RegressorMixin."""
        pass

    _LGBMBaseCrossValidator = None
    _LGBMLabelEncoder = None
    LGBMNotFittedError = ValueError
    _LGBMStratifiedKFold = None
    _LGBMGroupKFold = None
    _LGBMCheckXY = None
    _LGBMCheckArray = None
    _LGBMCheckSampleWeight = None
    _LGBMAssertAllFinite = None
    _LGBMCheckClassificationTargets = None
    _LGBMComputeSampleWeight = None

# pandas imports
try:
    from pandas import DataFrame as PdDataFrame
    from pandas import Series as PdSeries
    from pandas import concat

    try:
        from pandas import CategoricalDtype as PdCategoricalDtype
    except ImportError:
        from pandas.api.types import CategoricalDtype as PdCategoricalDtype

    PANDAS_INSTALLED = True
except ImportError:
    PANDAS_INSTALLED = False

    class PdSeries:  # type: ignore
        """Dummy class for pandas.Series."""
        def __init__(self, *args: Any, **kwargs: Any):
            pass

    class PdDataFrame:  # type: ignore
        """Dummy class for pandas.DataFrame."""
        def __init__(self, *args: Any, **kwargs: Any):
            pass

    class PdCategoricalDtype:  # type: ignore
        """Dummy class for pandas.CategoricalDtype."""
        def __init__(self, *args: Any, **kwargs: Any):
            pass

    concat = None

# matplotlib imports
try:
    import matplotlib  # noqa: F401
    MATPLOTLIB_INSTALLED = True
except ImportError:
    MATPLOTLIB_INSTALLED = False

# graphviz imports
try:
    import graphviz  # noqa: F401
    GRAPHVIZ_INSTALLED = True
except ImportError:
    GRAPHVIZ_INSTALLED = False

# datatable imports
try:
    import datatable

    if hasattr(datatable, "Frame"):
        dt_DataTable = datatable.Frame
    else:
        dt_DataTable = datatable.DataTable

    DATATABLE_INSTALLED = True
except ImportError:
    DATATABLE_INSTALLED = False

    class dt_DataTable:  # type: ignore
        """Dummy class for datatable.DataTable."""
        def __init__(self, *args: Any, **kwargs: Any):
            pass

# dask imports
try:
    from dask import delayed
    from dask.array import Array as DaskArray
    from dask.array import from_delayed as dask_array_from_delayed
    from dask.bag import from_delayed as dask_bag_from_delayed
    from dask.dataframe import DataFrame as DaskDataFrame
    from dask.dataframe import Series as DaskSeries
    from dask.distributed import Client, Future, default_client, wait

    DASK_INSTALLED = True
except (ImportError, ValueError):
    DASK_INSTALLED = False

    dask_array_from_delayed = None  # type: ignore[assignment]
    dask_bag_from_delayed = None  # type: ignore[assignment]
    delayed = None
    default_client = None  # type: ignore[assignment]
    wait = None  # type: ignore[assignment]

    class Client:  # type: ignore
        """Dummy class for dask.distributed.Client."""
        def __init__(self, *args: Any, **kwargs: Any):
            pass

    class Future:  # type: ignore
        """Dummy class for dask.distributed.Future."""
        def __init__(self, *args: Any, **kwargs: Any):
            pass

    class DaskArray:  # type: ignore
        """Dummy class for dask.array.Array."""
        def __init__(self, *args: Any, **kwargs: Any):
            pass

    class DaskDataFrame:  # type: ignore
        """Dummy class for dask.dataframe.DataFrame."""
        def __init__(self, *args: Any, **kwargs: Any):
            pass

    class DaskSeries:  # type: ignore
        """Dummy class for dask.dataframe.Series."""
        def __init__(self, *args: Any, **kwargs: Any):
            pass

# pyarrow imports
try:
    import pyarrow.compute as pa_compute
    from pyarrow import Array as PaArray
    from pyarrow import ChunkedArray as PaChunkedArray
    from pyarrow import Table as PaTable
    from pyarrow import chunked_array as pa_chunked_array
    from pyarrow.cffi import ffi as arrow_cffi
    from pyarrow.types import is_boolean as arrow_is_boolean
    from pyarrow.types import is_floating as arrow_is_floating
    from pyarrow.types import is_integer as arrow_is_integer

    PYARROW_INSTALLED = True
except ImportError:
    PYARROW_INSTALLED = False

    class PaArray:  # type: ignore
        """Dummy class for pyarrow.Array."""
        def __init__(self, *args: Any, **kwargs: Any):
            pass

    class PaChunkedArray:  # type: ignore
        """Dummy class for pyarrow.ChunkedArray."""
        def __init__(self, *args: Any, **kwargs: Any):
            pass

    class PaTable:  # type: ignore
        """Dummy class for pyarrow.Table."""
        def __init__(self, *args: Any, **kwargs: Any):
            pass

    class arrow_cffi:  # type: ignore
        """Dummy class for pyarrow.cffi.ffi."""
        CData = None
        addressof = None
        cast = None
        new = None

        def __init__(self, *args: Any, **kwargs: Any):
            pass

    class pa_compute:  # type: ignore
        """Dummy class for pyarrow.compute."""
        all = None
        equal = None

    pa_chunked_array = None
    arrow_is_boolean = None
    arrow_is_integer = None
    arrow_is_floating = None

# cpu_count() import and function
try:
    from joblib import cpu_count

    def _LGBMCpuCount(only_physical_cores: bool = True) -> int:
        return cpu_count(only_physical_cores=only_physical_cores)
except ImportError:
    try:
        from psutil import cpu_count

        def _LGBMCpuCount(only_physical_cores: bool = True) -> int:
            return cpu_count(logical=False) if only_physical_cores else cpu_count()
    except ImportError:
        from multiprocessing import cpu_count

        def _LGBMCpuCount(only_physical_cores: bool = True) -> int:
            return cpu_count()

__all__: List[str] = []
