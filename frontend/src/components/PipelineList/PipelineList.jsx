import React, { useState, useEffect } from 'react';
import { Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper, Chip, Typography, Box } from '@mui/material';
import { getPipelines } from '../../services/pipelineService';

function PipelineList() {
  const [pipelines, setPipelines] = useState([]);

  useEffect(() => {
    fetchPipelines();
  }, []);

  const fetchPipelines = async () => {
    try {
      const data = await getPipelines();
      setPipelines(data.pipelines);
    } catch (error) {
      console.error('Error fetching pipelines:', error);
    }
  };

  const getStatusColor = (status) => {
    switch (status) {
      case 'success': return 'success';
      case 'failed': return 'error';
      case 'running': return 'warning';
      default: return 'default';
    }
  };

  return (
    <Box>
      <Typography variant="h4" gutterBottom>Pipelines</Typography>
      
      <TableContainer component={Paper}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Name</TableCell>
              <TableCell>Platform</TableCell>
              <TableCell>Status</TableCell>
              <TableCell>Success Rate</TableCell>
              <TableCell>Avg Duration</TableCell>
              <TableCell>Last Run</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {pipelines.map((pipeline) => (
              <TableRow key={pipeline.id} hover>
                <TableCell>{pipeline.name}</TableCell>
                <TableCell>{pipeline.platform}</TableCell>
                <TableCell>
                  <Chip 
                    label={pipeline.status} 
                    color={getStatusColor(pipeline.status)} 
                    size="small" 
                  />
                </TableCell>
                <TableCell>{pipeline.success_rate}%</TableCell>
                <TableCell>{pipeline.avg_duration}s</TableCell>
                <TableCell>{new Date(pipeline.last_run).toLocaleString()}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </Box>
  );
}

export default PipelineList;
