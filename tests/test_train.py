from unittest import mock
import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from ml_model import train
from sklearn.linear_model import LinearRegression


@mock.patch("mlflow.sklearn.log_model")
@mock.patch("mlflow.log_metric")
@mock.patch("mlflow.start_run")
@mock.patch("mlflow.set_experiment")
def test_train_main_mocks(mock_set_experiment, mock_start_run, mock_log_metric, mock_log_model):
    # On mocke le contexte de run MLflow
    mock_start_run.return_value.__enter__.return_value = None

    # Exécute le main
    train.main()

    # Vérifie que l'expérience MLflow est bien définie
    mock_set_experiment.assert_called_once_with("/Users/anass.b.compt@gmail.com/diabetes-linear-regression")
    # Vérifie que le log du score a été appelé
    assert mock_log_metric.call_count == 1
    # Vérifie que le modèle a bien été loggué
    assert mock_log_model.call_count == 1

def test_train_runs_without_error():
    try:
        train.main()
    except Exception as e:
        pytest.fail(f"train.main() raised an exception: {e}") 