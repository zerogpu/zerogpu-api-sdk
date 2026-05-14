package main

import (
	"context"
	"fmt"
	"os"
	"strings"

	sdk "sdk"
	"sdk/client"
	"sdk/option"
)

func strPtr(s string) *string { return &s }

func main() {
	ctx := context.Background()
	apiKey := strings.TrimSpace(os.Getenv("ZEROGPU_API_KEY"))
	projectID := strings.TrimSpace(os.Getenv("ZEROGPU_PROJECT_ID"))
	model := strings.TrimSpace(os.Getenv("ZEROGPU_MODEL"))
	if apiKey == "" || projectID == "" {
		fmt.Fprintln(os.Stderr, "Set ZEROGPU_API_KEY and ZEROGPU_PROJECT_ID")
		os.Exit(1)
	}
	if model == "" {
		fmt.Fprintln(os.Stderr, "Set ZEROGPU_MODEL")
		os.Exit(1)
	}
	prompt := strings.TrimSpace(os.Getenv("ZEROGPU_INPUT_TEXT"))
	if prompt == "" {
		prompt = "In one short sentence, what is a habit tracker?"
	}

	c := client.NewClient(
		option.WithAPIKey(apiKey),
		option.WithProjectID(projectID),
	)

	msg := &sdk.InputMessage{}
	msg.SetRole(sdk.InputMessageRoleUser)
	msg.SetContent(prompt)

	textFormat := &sdk.TextResponseConfigFormat{}
	textFormat.SetType(strPtr("text"))
	textCfg := &sdk.TextResponseConfig{}
	textCfg.SetFormat(textFormat)

	req := &sdk.CreateResponseRequest{}
	req.SetModel(model)
	req.SetInput([]*sdk.InputMessage{msg})
	req.SetText(textCfg)

	res, err := c.Responses.CreateResponse(ctx, req)
	if err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
	fmt.Println("id:", res.GetID())
	fmt.Println("model:", res.GetModel())
	fmt.Println("usage:", res.GetUsage())
}
