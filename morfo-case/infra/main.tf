provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "raw_bucket" {
  bucket = "morfo-raw-bucket"
}

resource "aws_iam_role" "etl_execution_role" {
  name = "etl-execution-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Effect = "Allow",
      Principal = {
        Service = "batch.amazonaws.com"
      },
      Action = "sts:AssumeRole"
    }]
  })
}

resource "aws_iam_policy" "etl_s3_policy" {
  name        = "etl-s3-access"
  description = "Allow access to the raw bucket"
  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Action = [
        "s3:GetObject",
        "s3:PutObject",
        "s3:ListBucket"
      ],
      Resource = [
        "${aws_s3_bucket.raw_bucket.arn}",
        "${aws_s3_bucket.raw_bucket.arn}/*"
      ],
      Effect   = "Allow"
    }]
  })
}

resource "aws_iam_role_policy_attachment" "attach_s3_policy" {
  role       = aws_iam_role.etl_execution_role.name
  policy_arn = aws_iam_policy.etl_s3_policy.arn
}
