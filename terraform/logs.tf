# logs.tf

# Set up CloudWatch group and log stream and retain logs for 30 days
resource "aws_cloudwatch_log_group" "pg_log_group" {
  name              = "/ecs/pg-app"
  retention_in_days = 30

  tags = {
    Name = "pg-log-group"
  }
}

resource "aws_cloudwatch_log_stream" "pg_log_stream" {
  name           = "pg-log-stream"
  log_group_name = aws_cloudwatch_log_group.pg_log_group.name
}

