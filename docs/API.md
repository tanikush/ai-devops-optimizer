# API Documentation

## Base URL

```
http://localhost:8000/api/v1
```

## Authentication

Currently, the API doesn't require authentication. In production, add JWT tokens:

```
Authorization: Bearer <token>
```

## Endpoints

### Pipelines

#### Get All Pipelines
```
GET /pipelines/
```

Response:
```json
{
  "pipelines": [
    {
      "id": 1,
      "name": "main-pipeline",
      "platform": "github",
      "status": "success",
      "success_rate": 95.5,
      "avg_duration": 320
    }
  ]
}
```

#### Get Pipeline Details
```
GET /pipelines/{pipeline_id}
```

#### Get Pipeline Builds
```
GET /pipelines/{pipeline_id}/builds?limit=10
```

#### Create Pipeline
```
POST /pipelines/
Content-Type: application/json

{
  "name": "new-pipeline",
  "platform": "github",
  "repository": "org/repo",
  "branch": "main"
}
```

### Predictions

#### Predict Build Failure
```
POST /predictions/predict-failure
Content-Type: application/json

{
  "pipeline_id": 1,
  "files_changed": 5,
  "lines_added": 100,
  "test_count": 50
}
```

Response:
```json
{
  "prediction": "success",
  "confidence": 0.87,
  "probability_failure": 0.13,
  "probability_success": 0.87
}
```

#### Estimate Build Duration
```
POST /predictions/estimate-duration
Content-Type: application/json

{
  "pipeline_id": 1,
  "files_changed": 5,
  "test_count": 50
}
```

### Analytics

#### Get Overview
```
GET /analytics/overview
```

#### Get Trends
```
GET /analytics/trends?days=30
```

#### Get Pipeline Performance
```
GET /analytics/performance/{pipeline_id}?days=7
```

#### Get Bottlenecks
```
GET /analytics/bottlenecks/{pipeline_id}
```

### Recommendations

#### Get Recommendations
```
GET /recommendations/{pipeline_id}
```

Response:
```json
{
  "recommendations": [
    {
      "id": 1,
      "type": "performance",
      "priority": "high",
      "title": "Enable Parallel Test Execution",
      "estimated_time_saved": 120,
      "estimated_cost_saved": 45.50
    }
  ]
}
```

#### Apply Recommendation
```
POST /recommendations/{pipeline_id}/apply/{recommendation_id}
```

## Error Responses

All endpoints return standard HTTP status codes:

- 200: Success
- 201: Created
- 400: Bad Request
- 404: Not Found
- 500: Internal Server Error

Error format:
```json
{
  "detail": "Error message"
}
```

## Rate Limiting

Currently no rate limiting. In production, implement rate limiting per API key.

## Webhooks

Configure webhooks in your CI/CD platform to send events to:

```
POST /webhooks/{platform}
```

Supported platforms: github, jenkins, gitlab, circleci
