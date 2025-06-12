output "bucket_name" {
  value = aws_s3_bucket.raw_bucket.id
}

output "iam_role_arn" {
  value = aws_iam_role.etl_execution_role.arn
}
