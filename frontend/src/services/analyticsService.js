import api from './api';

export const getAnalyticsOverview = async () => {
  const response = await api.get('/api/v1/analytics/overview');
  return response.data;
};

export const getTrends = async (days = 30) => {
  const response = await api.get(`/api/v1/analytics/trends?days=${days}`);
  return response.data;
};

export const getPipelinePerformance = async (pipelineId, days = 7) => {
  const response = await api.get(`/api/v1/analytics/performance/${pipelineId}?days=${days}`);
  return response.data;
};

export const getBottlenecks = async (pipelineId) => {
  const response = await api.get(`/api/v1/analytics/bottlenecks/${pipelineId}`);
  return response.data;
};

export const comparePipelines = async (pipelineIds) => {
  const response = await api.get(`/api/v1/analytics/comparison?pipeline_ids=${pipelineIds.join(',')}`);
  return response.data;
};
