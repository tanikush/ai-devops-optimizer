import React, { useState, useEffect } from 'react';
import { Grid, Paper, Typography, Box, Card, CardContent } from '@mui/material';
import { Line } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend } from 'chart.js';
import { getAnalyticsOverview, getTrends } from '../../services/analyticsService';
import RocketLaunchIcon from '@mui/icons-material/RocketLaunch';
import TrendingUpIcon from '@mui/icons-material/TrendingUp';
import AttachMoneyIcon from '@mui/icons-material/AttachMoney';
import SpeedIcon from '@mui/icons-material/Speed';

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);

function Dashboard() {
  const [overview, setOverview] = useState(null);
  const [trends, setTrends] = useState(null);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const overviewData = await getAnalyticsOverview();
      const trendsData = await getTrends(7);
      setOverview(overviewData);
      setTrends(trendsData);
    } catch (error) {
      console.error('Error fetching dashboard data:', error);
    }
  };

  const chartData = trends ? {
    labels: trends.trends.map(t => t.date),
    datasets: [
      {
        label: 'Total Builds',
        data: trends.trends.map(t => t.total_builds),
        borderColor: 'rgb(75, 192, 192)',
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        tension: 0.4,
      },
      {
        label: 'Success Rate (%)',
        data: trends.trends.map(t => t.success_rate),
        borderColor: 'rgb(54, 162, 235)',
        backgroundColor: 'rgba(54, 162, 235, 0.2)',
        tension: 0.4,
      }
    ]
  } : null;

  if (!overview) return <Typography>Loading...</Typography>;

  return (
    <Box>
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

        {/* Chart */}
        <Grid item xs={12}>
          <Paper sx={{ p: 3, boxShadow: 3 }}>
            <Typography variant="h5" gutterBottom sx={{ fontWeight: 'bold' }}>
              📊 Build Trends (Last 7 Days)
            </Typography>
            {chartData && <Line data={chartData} options={{ responsive: true, maintainAspectRatio: true }} />}
          </Paper>
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
      </Grid>
    </Box>
  );
}

export default Dashboard;
