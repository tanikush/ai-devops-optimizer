import api from './api';

export const getPipelines = async () => {
  const response = await api.get('/api/v1/pipelines/');
  return response.data;
};

export const getPipeline = async (pipelineId) => {
  const response = await api.get(`/api/v1/pipelines/${pipelineId}`);
  return response.data;
};

export const getPipelineBuilds = async (pipelineId, limit = 10) => {
  const response = await api.get(`/api/v1/pipelines/${pipelineId}/builds?limit=${limit}`);
  return response.data;
};

export const createPipeline = async (pipelineData) => {
  const response = await api.post('/api/v1/pipelines/', pipelineData);
  return response.data;
};

export const updatePipeline = async (pipelineId, pipelineData) => {
  const response = await api.put(`/api/v1/pipelines/${pipelineId}`, pipelineData);
  return response.data;
};

export const deletePipeline = async (pipelineId) => {
  const response = await api.delete(`/api/v1/pipelines/${pipelineId}`);
  return response.data;
};
