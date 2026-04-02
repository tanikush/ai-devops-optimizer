import React, { useState, useEffect } from 'react';
import { Grid, Paper, Typography, Box, Card, CardContent, CircularProgress, Alert } from '@mui/material';
import RocketLaunchIcon from '@mui/icons-material/RocketLaunch';
import TrendingUpIcon from '@mui/icons-material/TrendingUp';
import AttachMoneyIcon from '@mui/icons-material/AttachMoney';
import SpeedIcon from '@mui/icons-material/Speed';

function Dashboard() {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [overview, setOverview] = useState(null);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      setLoading(true);
      
      // Try to fetch from API
      const response = await fetch('http://localhost:8000/api/v1/analytics/overview');
      
      if (!response.ok) {
        throw new Error('API not responding');
      }
      
      const data = await response.json();
      setOverview(data);
      setError(null);
    } catch (err) {
      console.error('Error fetching data:', err);
      
      // Use mock data if API fails
      setOverview({
        total_pipelines: 15,
        total_builds: 5420,
        success_rate: 91.5,
        avg_build_time: 342,
        total_time_saved: 12500,
        cost_savings: 2340.50
      });
      
      setError('Using demo data - Backend API not connected');
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <Box sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '50vh', flexDirection: 'column' }}>
        <CircularProgress size={60} />
        <Typography variant="h6" sx={{ mt: 2 }}>Loading Dashboard...</Typography>
        <Typography variant="body2" color="textSecondary" sx={{ mt: 1 }}>
          Connecting to backend API at http://localhost:8000
        </Typography>
      </Box>
    );
  }

  return (
    <Box>
      {error && (
        <Alert severity="warning" sx={{ mb: 3 }}>
          {error} - Make sure backend is running at http://localhost:8000
        </Alert>
      )}

      <Box sx={{ mb: 4 }}>
        <Typography variant="h3" gutterBottom sx={{ fontWeight: 'bold', color: '#1976d2' }}>
          🚀 Welcome to Your DevOps Command Center
        </Typography>
        <Typography variant="subtitle1" color="textSecondary">
          AI-Powered Pipeline Intelligence at Your Fingertips
        </Typography>
      </Box>
      
      <Grid container spacing={3}>
        {/* Metric Cards with Icons */}
        <Grid item xs={12} sm={6} md={3}>
          <Card sx={{ background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)', color: 'white' }}>
            <CardContent>
              <Box sx={{ display: 'flex', alignItems: 'center', mb: 1 }}>
                <RocketLaunchIcon sx={{ fontSize: 40, mr: 1 }} />
                <Typography variant="h3" sx={{ fontWeight: 'bold' }}>{overview.total_pipelines}</Typography>
              </Box>
              <Typography variant="body2">Active Pipelines</Typography>
            </CardContent>
          </Card>
        </Grid>
        
        <Grid item xs={12} sm={6} md={3}>
          <Card sx={{ background: 'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)', color: 'white' }}>
            <CardContent>
              <Box sx={{ display: 'flex', alignItems: 'center', mb: 1 }}>
                <TrendingUpIcon sx={{ fontSize: 40, mr: 1 }} />
                <Typography variant="h3" sx={{ fontWeight: 'bold' }}>{overview.total_builds}</Typography>
              </Box>
              <Typography variant="body2">Total Builds</Typography>
            </CardContent>
          </Card>
        </Grid>
        
        <Grid item xs={12} sm={6} md={3}>
          <Card sx={{ background: 'linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)', color: 'white' }}>
            <CardContent>
              <Box sx={{ display: 'flex', alignItems: 'center', mb: 1 }}>
                <SpeedIcon sx={{ fontSize: 40, mr: 1 }} />
                <Typography variant="h3" sx={{ fontWeight: 'bold' }}>{overview.success_rate}%</Typography>
              </Box>
              <Typography variant="body2">Success Rate</Typography>
            </CardContent>
          </Card>
        </Grid>
        
        <Grid item xs={12} sm={6} md={3}>
          <Card sx={{ background: 'linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)', color: 'white' }}>
            <CardContent>
              <Box sx={{ display: 'flex', alignItems: 'center', mb: 1 }}>
                <AttachMoneyIcon sx={{ fontSize: 40, mr: 1 }} />
                <Typography variant="h3" sx={{ fontWeight: 'bold' }}>${overview.cost_savings}</Typography>
              </Box>
              <Typography variant="body2">Cost Saved</Typography>
            </CardContent>
          </Card>
        </Grid>

        {/* Stats Cards */}
        <Grid item xs={12} md={6}>
          <Paper sx={{ p: 3, background: 'linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%)' }}>
            <Typography variant="h5" gutterBottom sx={{ fontWeight: 'bold' }}>⏱️ Time Saved</Typography>
            <Typography variant="h3" color="primary" sx={{ fontWeight: 'bold' }}>{overview.total_time_saved} min</Typography>
            <Typography variant="body2" color="textSecondary">Through AI optimizations</Typography>
          </Paper>
        </Grid>

        <Grid item xs={12} md={6}>
          <Paper sx={{ p: 3, background: 'linear-gradient(135deg, #a1c4fd 0%, #c2e9fb 100%)' }}>
            <Typography variant="h5" gutterBottom sx={{ fontWeight: 'bold' }}>🎯 Avg Build Time</Typography>
            <Typography variant="h3" color="primary" sx={{ fontWeight: 'bold' }}>{overview.avg_build_time}s</Typography>
            <Typography variant="body2" color="textSecondary">Across all pipelines</Typography>
          </Paper>
        </Grid>

        {/* Quick Actions */}
        <Grid item xs={12}>
          <Paper sx={{ p: 3, background: '#f5f5f5' }}>
            <Typography variant="h6" gutterBottom sx={{ fontWeight: 'bold' }}>🚀 Quick Actions</Typography>
            <Box sx={{ display: 'flex', gap: 2, flexWrap: 'wrap', mt: 2 }}>
              <Card sx={{ minWidth: 200, cursor: 'pointer', '&:hover': { boxShadow: 6 } }}>
                <CardContent>
                  <Typography variant="h6">View Pipelines</Typography>
                  <Typography variant="body2" color="textSecondary">Manage your CI/CD pipelines</Typography>
                </CardContent>
              </Card>
              <Card sx={{ minWidth: 200, cursor: 'pointer', '&:hover': { boxShadow: 6 } }}>
                <CardContent>
                  <Typography variant="h6">Get Predictions</Typography>
                  <Typography variant="body2" color="textSecondary">AI-powered build predictions</Typography>
                </CardContent>
              </Card>
              <Card sx={{ minWidth: 200, cursor: 'pointer', '&:hover': { boxShadow: 6 } }}>
                <CardContent>
                  <Typography variant="h6">View Recommendations</Typography>
                  <Typography variant="body2" color="textSecondary">Optimization suggestions</Typography>
                </CardContent>
              </Card>
            </Box>
          </Paper>
        </Grid>

        {/* API Status */}
        <Grid item xs={12}>
          <Paper sx={{ p: 2, background: error ? '#fff3e0' : '#e8f5e9' }}>
            <Typography variant="body2">
              <strong>Backend Status:</strong> {error ? '⚠️ Disconnected (using demo data)' : '✅ Connected'}
            </Typography>
            <Typography variant="caption" color="textSecondary">
              API Endpoint: http://localhost:8000/api/v1/analytics/overview
            </Typography>
          </Paper>
        </Grid>
      </Grid>
    </Box>
  );
}

export default Dashboard;
