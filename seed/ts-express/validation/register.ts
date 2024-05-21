/**
 * This file was auto-generated by Fern from our API Definition.
 */

import express from "express";
import { RootService } from "./api/service/RootService";

export function register(
    expressApp: express.Express | express.Router,
    services: {
        _root: RootService;
    }
): void {
    (expressApp as any).use("/", services._root.toRouter());
}