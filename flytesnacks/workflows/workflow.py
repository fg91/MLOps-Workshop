import logging
from typing import Tuple

from flytekit import task, workflow


logging.getLogger().setLevel(logging.INFO)


@task
def prepare_data() -> str:
    """Download a dataset, validate it, and return blob storage uri."""
    logging.info("Data prepared")
    return "uri"

@task
def train_model(data_uri: str) -> Tuple[str, str]:
    """
    Train and evaluate model on prepared data at `data_uri`.

    Args:
        data_uri (str): uri of prepared data in blob storage.

    Returns:
        run_id (str): the id of the Mlflow run
        artifact_uri (str): the blob storage uri of the model artifact
    """
    logging.info("Model trained and evaluated")
    return "run_id", "artifact_uri"


@task
def deploy_model(run_id: str, model_uri: str) -> str:
    """
    Deploy the model saved at model_uri and test the deployed model.
    Args:
        run_id (str): the Mlflow run id of the training run for which the model is deployed
        model_uri (str): the blob storage uri of the model artifact to be deployed
    Returns:
        endpoint_uri (str): the path of the deployed model endpoint.
    """
    logging.info("Model deployed and tested")
    return "endpoint_uri"


@workflow
def pipeline() -> str:
    data_uri = prepare_data()
    run_id, artifact_uri = train_model(data_uri=data_uri)
    endpoint_uri = deploy_model(run_id=run_id, model_uri=artifact_uri)
    
    return endpoint_uri


if __name__ == "__main__":
    logging.info(pipeline())
