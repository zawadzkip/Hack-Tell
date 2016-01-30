//
//  ViewController.swift
//  DoorBell
//
//  Created by Patrick Zawadzki on 1/30/16.
//  Copyright © 2016 PatZawadzki. All rights reserved.
//

import UIKit
import CocoaAsyncSocket
class ViewController: UIViewController {


    
    @IBOutlet weak var ipTextField: UITextField!
    @IBOutlet weak var clipTextField: UITextField!
    var port:UInt16 = 12000;
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    @IBAction func testSendPressed(sender: UIButton) {
        let mySocket = GCDAsyncUdpSocket();
        let data = clipTextField.text!.dataUsingEncoding(NSUTF8StringEncoding)
        mySocket.setIPv4Enabled(true)
        mySocket.sendData(data, toHost: ipTextField.text!, port: port, withTimeout: 4, tag: 0)
        
    }


}

