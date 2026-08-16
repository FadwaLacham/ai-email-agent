/**
=========================================================
* Material Dashboard 2 React - AI Email Agent
=========================================================
*/

import { useEffect, useState } from "react";

// @mui material components
import Grid from "@mui/material/Grid";
import Card from "@mui/material/Card";
import TextField from "@mui/material/TextField";
import MenuItem from "@mui/material/MenuItem";
import Button from "@mui/material/Button";

// Material Dashboard components
import MDBox from "components/MDBox";
import MDTypography from "components/MDTypography";

// Layout components
import DashboardLayout from "examples/LayoutContainers/DashboardLayout";
import DashboardNavbar from "examples/Navbars/DashboardNavbar";
import Footer from "examples/Footer";

// Table component
import DataTable from "examples/Tables/DataTable";

// Axios
import api from "api/axios";

function Tables() {
  const [emails, setEmails] = useState([]);

  // Filters

  const [search, setSearch] = useState("");

  const [priority, setPriority] = useState("");

  const [category, setCategory] = useState("");

  const [importance, setImportance] = useState("");

  const fetchEmails = () => {
    let url = "https://ai-email-agent-backend.fastapicloud.dev/emails?";

    if (search) {
      url += `search=${search}&`;
    }

    if (priority) {
      url += `priority=${priority}&`;
    }

    if (category) {
      url += `category=${category}&`;
    }

    if (importance) {
      url += `importance=${importance}&`;
    }

    api

      .get(url)

      .then((response) => {
        setEmails(response.data);
      })

      .catch((error) => {
        console.log("API ERROR:", error);
      });
  };

  useEffect(() => {
    fetchEmails();
  }, [search, priority, category, importance]);

  const resetFilters = () => {
    setSearch("");

    setPriority("");

    setCategory("");

    setImportance("");
  };

  const columns = [
    {
      Header: "Sender",
      accessor: "sender",
      align: "left",
    },

    {
      Header: "Subject",
      accessor: "subject",
      align: "left",
    },

    {
      Header: "Category",
      accessor: "category",
      align: "center",
    },

    {
      Header: "Priority",
      accessor: "priority",
      align: "center",
    },

    {
      Header: "Score",
      accessor: "score",
      align: "center",
    },

    {
      Header: "Decision",
      accessor: "decision",
      align: "center",
    },
  ];

  const rows = emails.map((email) => ({
    sender: email.sender,

    subject: email.subject,

    category: email.category,

    priority: email.priority,

    score: email.score,

    decision: email.decision,
  }));

  return (
    <DashboardLayout>
      <DashboardNavbar />

      <MDBox pt={6} pb={3}>
        {/* ================= FILTERS ================= */}
        <Card sx={{ mb: 5 }}>
          <MDBox p={3}>
            <Grid container spacing={2} alignItems="center">
              {/* Search */}

              <Grid item xs={12} md={4}>
                <TextField
                  fullWidth
                  variant="outlined"
                  label="Search emails"
                  placeholder="Sender or subject"
                  value={search}
                  onChange={(e) => setSearch(e.target.value)}
                />
              </Grid>

              {/* Priority */}

              <Grid item xs={12} md={2}>
                <MDBox>
                  <TextField
                    select
                    fullWidth
                    label="Priority"
                    value={priority}
                    onChange={(e) => setPriority(e.target.value)}
                    sx={{
                      "& .MuiInputBase-root": {
                        height: "45px",
                      },
                    }}
                  >
                    <MenuItem value="">All</MenuItem>

                    <MenuItem value="HIGH">HIGH</MenuItem>

                    <MenuItem value="MEDIUM">MEDIUM</MenuItem>

                    <MenuItem value="LOW">LOW</MenuItem>
                  </TextField>
                </MDBox>
              </Grid>

              {/* Category */}

              <Grid item xs={12} md={2}>
                <TextField
                  fullWidth
                  variant="outlined"
                  label="Category"
                  placeholder="Work"
                  value={category}
                  onChange={(e) => setCategory(e.target.value)}
                />
              </Grid>

              {/* Importance */}

              <Grid item xs={12} md={2}>
                <MDBox>
                  <TextField
                    select
                    fullWidth
                    label="Importance"
                    value={importance}
                    onChange={(e) => setImportance(e.target.value)}
                    sx={{
                      "& .MuiInputBase-root": {
                        height: "45px",
                      },
                    }}
                  >
                    <MenuItem value="">All</MenuItem>

                    <MenuItem value="HIGH">HIGH</MenuItem>

                    <MenuItem value="LOW">LOW</MenuItem>
                  </TextField>
                </MDBox>
              </Grid>
              {/* Reset */}

              <Grid item xs={12} md={2}>
                <Button
                  fullWidth
                  variant="contained"
                  color="info"
                  sx={{
                    height: "56px",
                  }}
                  onClick={resetFilters}
                >
                  RESET
                </Button>
              </Grid>
            </Grid>
          </MDBox>
        </Card>
        <Grid container spacing={6}>
          <Grid item xs={12}>
            <Card>
              <MDBox
                mx={2}
                mt={-3}
                py={3}
                px={2}
                variant="gradient"
                bgColor="info"
                borderRadius="lg"
                coloredShadow="info"
              >
                <MDTypography variant="h6" color="white">
                  Processed Emails
                </MDTypography>
              </MDBox>

              <MDBox pt={3}>
                <DataTable
                  table={{
                    columns,

                    rows,
                  }}
                  isSorted={true}
                  entriesPerPage={true}
                  showTotalEntries={true}
                  noEndBorder
                />
              </MDBox>
            </Card>
          </Grid>
        </Grid>
      </MDBox>

      <Footer />
    </DashboardLayout>
  );
}

export default Tables;
