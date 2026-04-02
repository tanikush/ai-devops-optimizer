import api from './api';

export const getRecommendations = async (pipelineId) => {
  const response = await api.get(`/api/v1/recommendations/${pipelineId}`);
  return response.data;
};

export const applyRecommendation = async (pipelineId, recommendationId) => {
  const response = await api.post(`/api/v1/recommendations/${pipelineId}/apply/${recommendationId}`);
  return response.data;
};

export const getRecommendationHistory = async (pipelineId) => {
  const response = await api.get(`/api/v1/recommendations/${pipelineId}/history`);
  return response.data;
};

export const getGlobalInsights = async () => {
  const response = await api.get('/api/v1/recommendations/global/insights');
  return response.data;
};
