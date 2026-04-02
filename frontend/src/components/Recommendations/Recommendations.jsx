import React, { useState, useEffect } from 'react';
import { Typography, Box, Paper, Card, CardContent, Chip, Button, Grid } from '@mui/material';
import { getRecommendations } from '../../services/recommendationService';

function Recommendations() {
  const [recommendations, setRecommendations] = useState([]);

  useEffect(() => {
    fetchRecommendations();
  }, []);

  const fetchRecommendations = async () => {
    try {
      const data = await getRecommendations(1);
      setRecommendations(data.recommendations);
    } catch (error) {
      console.error('Error fetching recommendations:', error);
    }
  };

  const getPriorityColor = (priority) => {
    switch (priority) {
      case 'high': return 'error';
      case 'medium': return 'warning';
      case 'low': return 'info';
      default: return 'default';
    }
  };

  return (
    <Box>
      <Typography variant="h4" gutterBottom>Optimization Recommendations</Typography>
      
      <Grid container spacing={3}>
        {recommendations.map((rec) => (
          <Grid item xs={12} key={rec.id}>
            <Card>
              <CardContent>
                <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 2 }}>
                  <Typography variant="h6">{rec.title}</Typography>
                  <Chip label={rec.priority} color={getPriorityColor(rec.priority)} size="small" />
                </Box>
                
                <Typography variant="body2" color="textSecondary" paragraph>
                  {rec.description}
                </Typography>
                
                <Box sx={{ display: 'flex', gap: 2, mb: 2 }}>
                  <Chip label={`Time Saved: ${rec.estimated_time_saved}s`} variant="outlined" />
                  <Chip label={`Cost Saved: $${rec.estimated_cost_saved}`} variant="outlined" />
                  <Chip label={`Effort: ${rec.implementation_effort}`} variant="outlined" />
                </Box>
                
                <Button variant="contained" size="small">
                  Apply Recommendation
                </Button>
              </CardContent>
            </Card>
          </Grid>
        ))}
      </Grid>
    </Box>
  );
}

export default Recommendations;
