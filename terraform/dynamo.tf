resource "aws_dynamodb_table" "url_shortener_table" {
  name             = "urm-shortener"
  billing_mode     = "PAY_PER_REQUEST"
  hash_key         = "Id"
  stream_enabled   = true
  stream_view_type = "NEW_AND_OLD_IMAGES"

  attribute {
    name = "long_url"
    type = "S"
  }

  attribute {
    name = "slug"
    type = "S"
  }
}
