# type: ignore

from constructs import Construct
from aws_cdk_lib import ( 
    Stack,
    aws_s3 as s3, 
    aws_s3_deployment as s3_deploy
)

class CdkStaticWebsiteStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        #create a s3 bucket to host our static website
        static_website_bucket = s3.Bucket(self, "StaticS3Bucket",
            public_read_access=True,
            block_public_access=s3.BlockPublicAccess(restrict_public_buckets = False),
            website_index_document='index.html',
            website_error_document='error.html'
        )

        #upload the html documents from s3-assets/ directory to the s3 bucket
        deployment = s3_deploy.BucketDeployment(self, "DeployWebsite",
            sources=[s3_deploy.Source.asset("../s3-assets")],
            destination_bucket=static_website_bucket
        )
