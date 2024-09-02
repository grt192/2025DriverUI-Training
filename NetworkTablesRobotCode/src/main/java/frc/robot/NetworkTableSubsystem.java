package frc.robot;

import edu.wpi.first.networktables.NetworkTable;
import edu.wpi.first.networktables.NetworkTableEntry;
import edu.wpi.first.networktables.NetworkTableInstance;
import edu.wpi.first.wpilibj2.command.SubsystemBase;

class NetworkTableSubsystem extends SubsystemBase{

    private NetworkTableInstance networkTablesInstance;
    private NetworkTable networkTable;
    private NetworkTableEntry networkTableEntry;
    private double iterator = 0.0;

    public NetworkTableSubsystem(){
        // Initialize the NetworkTables
        networkTablesInstance = NetworkTableInstance.getDefault();
        networkTable = networkTablesInstance.getTable("networkTable");
        networkTableEntry = networkTable.getEntry("networkTableEntry");
        networkTableEntry.setDouble(iterator); 
    }

    @Override
    public void periodic(){
        // Update the NetworkTable Entry Value
        iterator += 0.01;
        networkTableEntry.setDouble(iterator); 
    }
}